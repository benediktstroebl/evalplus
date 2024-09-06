
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
    words = word.split()
    closest_vowel = ""

    if len(words) >= 2:
        if words[-2] not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            closest_vowel = words[-2]

    return closest_vowel

