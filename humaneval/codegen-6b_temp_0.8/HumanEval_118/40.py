
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
    vowel_first = ["a", "e", "i", "o", "u"]
    vowel_last = ["a", "e", "i", "o", "u", "y", "h", "w", "k", "r", "r"]
    vowel_chars = ["a", "e", "i", "o", "u"]
    for i in range(1, len(word)):
        if word[-i] in vowel_chars:
            return word[-i]
        if word[-i] in vowel_first:
            return word[-1]
        if word[-i] in vowel_last:
            return word[-i]
    return ""
