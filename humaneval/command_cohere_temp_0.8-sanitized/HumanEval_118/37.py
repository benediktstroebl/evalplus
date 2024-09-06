def get_closest_vowel(word):
    """
    Find the closest vowel to the right of consonant sequences within a word.
    """
    
    # Split the word into individual characters and initialize the closest vowel found.
    word_list = list(word)
    closest_vowel = ''
    
    # Iterate through the word from right to left.
    for i in range(1, len(word_list)):
        # Check if the current character is a consonant.
        if word_list[i].lower() not in 'aeuio':
            # If the previous character is a vowel, assign it as the closest vowel.
            if i > 0 and word_list[i-1].lower() in 'aeuio':
                closest_vowel = word_list[i-1]
            # If a consonant sequence is found, break out of the loop.
            else:
                break
    
    # Return the found closest vowel or an empty string.
    return closest_vowel or ''