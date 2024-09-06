def split_words(txt):
    ans = txt.split(",")
    if len(ans) > 0:
        return ans
    else:
        ls = txt.split()
        if len(ls) > 0:
            return ls
        else:
            return len(txt.lower())%2