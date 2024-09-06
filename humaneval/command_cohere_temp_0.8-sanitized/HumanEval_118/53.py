def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming vowels at the start and end do not count.
    Empty string if no fitting vowel is found.
    
    Args:
        word (str): The input word
    
    Returns:
        str: The closest vowel to the right meeting the criteria or an empty string.
    """
    # Define the vowels to help with finding a match
    vowels = 'AEIOUaeiou'
    
    # Check if the word has at least 2 characters and prune if not to avoid error prone cases
    if len(word) < 2:
        return ''

    # Initialize the result to an empty string
    result = ''

    # Ensure the last character of the word is not a vowel, and that the word is not just a vowel
    if word[-1] in vowels and word != '*':
        result = word[-1]

    # Iterate over each character starting from the second to last character to the second character
    for x in range(len(word)-2, 1, -1):
        if word[x] in vowels:
            result = word[x]
            break

    # Return the result
    return result