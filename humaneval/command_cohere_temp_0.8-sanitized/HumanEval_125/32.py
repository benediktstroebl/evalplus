def split_words(txt):
    ans = txt.split(",")
    if len(ans) == 1:
        ans = txt.split()
    if len(ans) == 1 and ans[0].isalpha():
        ans = len(ans[0]) % 2
    return ans