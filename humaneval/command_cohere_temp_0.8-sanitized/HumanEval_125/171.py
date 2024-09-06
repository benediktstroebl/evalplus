import re
def split_words(txt):
    ans = []
    txt = re.sub('[^a-zA-Z0-9]', '', txt)
    if txt:
        if ',' in txt:
            ans = txt.split(',')
        elif ' ' in txt:
            ans = txt.split()
        else:
            ans = [txt]
    else:
        ans = []
    return ans