def split_words(txt):
    ans = txt.split(",")
    if len(ans) == 1:
        if ' ' in txt:
            ans = txt.split(" ")
        else:
            ans = len(txt)
    return ans