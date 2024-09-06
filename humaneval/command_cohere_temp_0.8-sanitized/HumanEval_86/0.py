def anti_shuffle(s):
    words = s.split()
    ordered = ' '.join(char_ordered(word) for word in words)
    return ordered
def char_ordered(word):
    ascii_sorted = [char for char in word if char != ' ']
    return ''.join(ascii_sorted)