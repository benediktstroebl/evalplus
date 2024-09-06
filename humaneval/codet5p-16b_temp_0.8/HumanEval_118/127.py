
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

    closest_vowel = ""

    def is_vowel(letter):
        return letter in ["a", "e", "i", "o", "u"]

    for index, letter in enumerate(word[::-1]):
        if not is_vowel(letter) and not is_vowel(word[-index - 2]):
            break
        else:
            closest_vowel = word[-index - 1]
    
    return closest_vowel

