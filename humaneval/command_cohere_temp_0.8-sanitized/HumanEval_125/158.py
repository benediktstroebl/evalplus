def split_words(txt):
    words = []
    has_alpha = False
    for c in txt:
        if c.isalpha():
            has_alpha = True
        if c.islower() and ord(c) % 2 == 0:
            words.append(c)
    if has_alpha: 
        words = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else []
    return words