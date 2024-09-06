def anti_shuffle(s):
    # Split the string into individual words and flip them
    words = sorted(s.split(), key=lambda x: x.encode())
    flipped_words = [char for word in words for char in word]
    # Join them back together and return the ordered string
    return ' '.join(flipped_words)