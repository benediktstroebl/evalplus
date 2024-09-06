def anti_shuffle(s):
    # Split the string into individual words and store the word and its length.
    words = [(word, len(word)) for word in s.split()]
    
    # Sort the words based on the length and then alphabetically. Now, join them back.
    sorted_words = ' '.join(sorted(words, key=lambda x: (x[1], x[0])))
    
    # Now, replace each word with a new word formed by arranging characters in ascending order.
    ascii_sorted_words = [char.encode(encoding='ascii').decode(encoding='ascii') for char in sorted(word) if len(word) > 1]
    new_words = [''.join(char) for char in ascii_sorted_words]
    
    final_str = ' '.join(new_words)
    return final_str