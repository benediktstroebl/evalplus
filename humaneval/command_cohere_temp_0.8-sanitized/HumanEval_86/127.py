def anti_shuffle(s):
    # Split the string into individual words
    words = s.split()
    # Initialize an empty string to build the ordered string
    ordered_str = ""
    # Iterate through each word in the string
    for word in words:
        # Split the word into individual characters and sort them based on ASCII value
        sorted_word = ''.join(sorted(word, key=str.ascii_lower))
        # Add the sorted word to the ordered string
        ordered_str += sorted_word + " "
    # Remove the extra space at the end and return the ordered string
    return ordered_str.rstrip()