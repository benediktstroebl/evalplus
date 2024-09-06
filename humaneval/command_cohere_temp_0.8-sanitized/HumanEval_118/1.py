def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming vowels at the start and end do not count.
    Empty string if no qualifying vowel is found.
    """
    # Ensure input is lowercase to make matching simpler and consistent with the statement's case sensitivity
    word = word.lower()
    # Ensure we have at least 2 consonants to squeeze a vowel in between
    if len(word) < 3: return ''
    
    # Find indices of possible ending consonants
    word_end = len(word) - 1
    consonant_right_end = word_end
    while word[consonant_right_end] in 'aeiou':
        consonant_right_end -= 1

    # If there are no consonants on the right, return the last vowel
    if consonant_right_End < 0:
        return word[word_end]

    # Find the closest vowel to the right of the right-most consonant
    vowel_right_of_consonant = ''
    for char in word[consonant_right_end+1:]:
        if char in 'aeiou':
            vowel_right_of_consonant = char
            break

    return vowel_right_of_consonant