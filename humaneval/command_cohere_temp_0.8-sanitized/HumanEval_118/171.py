def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming the vowels occur between two consonants.
    Ignores starting and ending vowels.
    """
    vowels = 'AEIOUaeiou'  
    # Stripping punctuation and converting to lower case for the sake of the exercise
    cleaned = word.strip('.,?!''()"():;').lower()
    result = ''
    # Looking for vowels at the edges and within the word
    for char in cleaned:
        if char in vowels:
            if not result or abs(result in vowels - char) < abs(result - char):
                result = char
    return result