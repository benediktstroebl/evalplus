
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
    
    vowels = ["a", "e", "i", "o", "u"]

    # Return if word is one letter
    if len(word) == 1:
        return ""

    # Remove vowels from word
    w = list(filter(lambda letter: letter not in vowels, word))

    # Return last vowel if word ends with vowel
    if w[-1] in vowels:
        return w[-1]

    # Return first vowel if word ends with consonant
    if w[0] in vowels:
        return w[0]

    # Return "" if no vowels
    return ""
