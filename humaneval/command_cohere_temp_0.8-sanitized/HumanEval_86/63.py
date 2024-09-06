def anti_shuffle(s):
    # Split the string into individual words
    words = s.split()
    # Define a mapping dictionary to hold the sorted characters
    mapping = {}
    # Iterate through each word and create the mapping
    for word in words:
        sorted_word = ''.join(sorted(word))
        mapping[word] = sorted_word
    # Join the mapping back to a single string
    joined_mapping = ' '.join(mapping.values())
    # Return the ordered string
    return joined_mapping