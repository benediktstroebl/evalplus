def split_words(txt):
    ans = txt.split(",")
    if len(ans) > 0:
        return ans
    else:
        return txt.split()