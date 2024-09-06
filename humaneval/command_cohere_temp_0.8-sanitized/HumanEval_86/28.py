def anti_shuffle(s):
    words = s.split()
    res = ' '.join(char_sorted(word) for word in words)
    return res.strip()
def char_sorted(word):
    return ''.join(sorted(word))