def anti_shuffle(s):
    # Replace all words with a new word where characters are arranged in ascending order
    # Based on ascii values, while keeping the order of words and blank spaces.
    new_word = ''.join(chr(c) for c in sorted(s.replace(" ", "").encode()))
    return ' '.join(e for e in s.split() if e != ' ') + ' ' + new_word