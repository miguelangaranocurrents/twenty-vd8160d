import json, sys, os

path, needle = sys.argv[1], sys.argv[2]
d = os.path.dirname(path)
for line in open(path):
    e = json.loads(line)
    s = e.get('snapshot', {})
    req = s.get('request', {})
    pd = req.get('postData') or {}
    txt = pd.get('text', '') if isinstance(pd, dict) else ''
    if not txt and isinstance(pd, dict) and pd.get('_sha1'):
        try:
            txt = open(os.path.join(d, 'resources', pd['_sha1'])).read()
        except Exception:
            pass
    if needle in txt:
        print('REQ', txt[:2500])
        c = s.get('response', {}).get('content', {})
        sha = c.get('_sha1')
        if sha:
            print('RESP', open(os.path.join(d, 'resources', sha)).read()[:2500])
        print('-----')
