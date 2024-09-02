
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

    closest_vowel = ''

    for i, char in enumerate(word):
        if char in 'aiueo': # All vowels
            if closest_vowel:
                if abs(i-len(word)) > abs(i-len(closest_vowel)):
                    closest_vowel = char
            else:
                closest_vowel = char
    return closest_vowel


