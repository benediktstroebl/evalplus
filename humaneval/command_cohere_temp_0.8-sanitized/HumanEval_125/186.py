def split_words(txt):
    ans = txt.split(",")
    if len(ans) == 1:
        ans = txt.split()
    if len(ans) == 1:
        return len([char for char in txt if char.islower() and ord(char) % 2 == 0])
    return ans