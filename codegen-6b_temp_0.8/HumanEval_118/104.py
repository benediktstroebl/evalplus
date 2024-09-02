
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
    if word[0] in ["a", "e", "i", "o", "u"]:
        return word[0]
    if word[-1] in ["a", "e", "i", "o", "u"]:
        return word[-1]
    if len(word) < 2:
        return ""
    ind = 0
    for i, letter in enumerate(reversed(word)):
        if letter in ["a", "e", "i", "o", "u"]:
            ind = len(word) - i
            break
    if ind == 0:
        return ""
    return word[ind:]

