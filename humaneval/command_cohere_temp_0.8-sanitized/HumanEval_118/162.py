def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming vowels at the start and end of a word don't count.
    Empty string if no qualifying vowel found.
    
    Args:
        word (str): Input word with only English letters.
    
    Returns:
        str: Closest vowel to the right of the word, or empty string.
    """
    # Ensure the input is case-sensitive and only contains alphabetic characters
    validation_message = "The input word {} is invalid. Ensure the input is a case-sensitive string of English letters only."
    assert all(char.isalpha() for char in word), validation_message.assertion_msg(word)
    assert all(char.isalpha() for char in word), validation_message

    # Define valid vowels and initial/final positions
    vowels = set('AEIOUaeiou')
    start, end = 0, len(word) - 1

    # Define direction (right) and initialize result, iterating through potential vowels
    direction = 1
    result = ""
    for char in word:
        if char in vowels and word[start:char][0] != char and word[char:end][-1] != char:
            result = char
            break

    return result