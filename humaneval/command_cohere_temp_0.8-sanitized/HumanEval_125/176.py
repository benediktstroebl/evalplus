import re
def split_words(txt):
    ans = re.findall(r'\w+|[.,]', txt)
    if len(ans) == 1 and ans[0].isalpha():
        return len(ans[0])
    return ans