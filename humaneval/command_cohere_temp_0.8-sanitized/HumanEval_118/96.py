def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming the vowels occur between two consonants.
    Ignores starting and ending vowels.
    """
    # Ensure input is lowercase
    word = word.lower()
    # Split the word into individual characters and initialize the right-most vowel and its distance
    vowel, dist = None, float('inf')
    # Iterate over each character in the word
    for char in word:
        if char in 'aeiou':
            if char != word[0] and word[-1] != char:
                dist = 1
                vowel = char
            elif dist > 1 and char in 'eiou':
                dist, vowel = 1, char
    # Return the found vowel or an empty string
    return vowel or ''