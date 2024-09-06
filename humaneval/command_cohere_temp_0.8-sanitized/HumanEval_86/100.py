def anti_shuffle(s):
    """
    Returns an ordered version of the input string, where each word is sorted
    based on ASCII values while maintaining the original word order and spaces.
    
    Args:
        s (str): Input string to be ordered.

    Returns:
        str: Ordered version of the input string.
    """
    # Split the input string into individual words and blank spaces
    word_array = s.split()

    # Initialize a new array to store the sorted words
    new_word_array = []
    
    # Iterate through each word in the original string
    for word in word_array:
        # Sort the characters of each word based on ASCII values
        ascii_sorted = ''.join(sorted(word))
        
        # Add the sorted word to the new array
        new_word_array.append(ascii_sorted)
    
    # Join the sorted words with spaces to form the final ordered string
    return ' '.join(new_word_array)