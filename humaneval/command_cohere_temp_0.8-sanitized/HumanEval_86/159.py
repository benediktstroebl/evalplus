def anti_shuffle(s):
    # Split the input string into individual words
    words = s.split()
    # Initialize an empty string to build the ordered result
    result = ""
    
    # Iterate through each word in the input string
    for word in words:
        # Sort the characters of each word based on ASCII values
        sorted_word = ''.join(sorted(word))
        # Add the sorted word to the result string
        result += sorted_word + " "
    
    # Remove the extra space at the end of the result string
    return result.rstrip()