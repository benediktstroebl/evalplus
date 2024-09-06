def split_words(txt):
    ans = txt.split(",")
    if len(ans) > 0:
        return ans
    elif " " in txt:
        return txt.split(" ")
    else:
        return len(txt)