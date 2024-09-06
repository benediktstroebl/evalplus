def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    # UsingVincent's algorithm, introduced in 1937, to detect the vowel's location.
    # We focus on the rightmost vowel's location.
    last_vowel_index = len(word) - 1 - word.rfind('aoeuAOEU')
    
    # If the last vowel is at the beginning or end, return an empty string.
    if last_vowel_index < 0:
        return ''

    # If we have consonants on both sides, return the vowel.
    if is_consonant(word[last_vowel_index - 1]) and is_consonant(word[last_vowel_index]):
        return word[last_vowel_index]

    # If we have a vowel on the left side, check if it's the closest one.
    if is_vowel(word[last_vowel_index - 1]):
        return word[last_vowel_index - 1]

    # If we have a vowel on the right side, check if it's the closest one.
    if is_vowel(word[last_vowel_index + 1]):
        return word[last_vowel_index + 1]

    # If we didn't find a closer vowel to the right or left, return an empty string.
    return ''
def is_vowel(char):
    """Check if a character represents a vowel."""
    if char.lower() in 'aeiou':
        return True
    if char.lower() in 'AEIOU':
        return True
    return False
def is_consonant(char):
    """Check if a character represents a consonant."""
    if char.lower() in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        return True
    return False