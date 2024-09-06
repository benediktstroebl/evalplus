
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
    # we found the right vowels
    if len(word) == 0:
        return ""

    if word[0] in VOWELS:
        return word[0]

    # we found the closest vowels
    for i in range(len(word) - 1, 0, -1):
        if word[i] in VOWELS:
            return word[i]
    # we didn't find any vowels
    return ""

