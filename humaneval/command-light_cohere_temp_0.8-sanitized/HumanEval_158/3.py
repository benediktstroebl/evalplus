def find_max(words):
    # Create a dictionary to store character frequencies
    char_count = {}
    
    # Loop through the list of strings
    for word in words:
        # Convert the string to lowercase to ensure case insensitivity
        word = word.lower()
        
        # Add the electrodes in the dictionary
        char_count[word] = len(word)
    
    # Find the word with the maximum number of unique characters
    max_word = max(char_count, key=char_count.get)
    
    return max_word