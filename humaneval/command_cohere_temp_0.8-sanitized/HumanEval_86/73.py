def anti_shuffle(s):
    word_inds = [i for i, char in enumerate(s.split()) if char != ' ' and char != '']
    sorted_words = [chr(min(ord(char), len(char) - 1) for char in s.split()[word_inds]) for word_inds in word_inds]
    return ' '.join(sorted_words)