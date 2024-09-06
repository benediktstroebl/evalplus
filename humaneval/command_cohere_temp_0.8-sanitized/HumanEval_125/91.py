import re
def split_words(txt):
    ans = re.findall(r'\w+', txt)
    if len(ans) > 0:
        return ans
    else:
        commas = txt.split(',')
        if len(commas) > 1:
            return commas
        else:
            return len(txt)