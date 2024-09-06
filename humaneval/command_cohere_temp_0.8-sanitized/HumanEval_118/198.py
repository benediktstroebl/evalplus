def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming consonants sandwiching it.
    Ignores starting and ending vowels.
    """
    # Your code here.
    import re

    vowels = set('AEIOUaeiou')
    
    # Find a consonant in the right half of the word
    match = re.search(r'(?<!([aeiou]))([^aeiou]*?[aeiou])', word)
    
    # If found, check if it's followed by a closer vowel (case sensitive)
    if match:
        vowel = match.group(2)
        if vowel in vowels and word.lower() not in vowel.lower():
            return vowel
    return ''