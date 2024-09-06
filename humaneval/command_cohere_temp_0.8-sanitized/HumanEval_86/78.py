def anti_shuffle(s):
    words = s.split()
    sorted_alphabets = ''.join(sorted(word, key=str.ascii_lower))
    return ' '.join(words for word in words if word == sorted_alphabets)