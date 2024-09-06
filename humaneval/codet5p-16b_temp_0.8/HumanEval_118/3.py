
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

    vowels = "AEIOU"
    word = word[::-1]
    last_vowel = ""
    for i,c in enumerate(word):
        if c in vowels and not last_vowel:
            last_vowel = c
            continue
        if c in vowels and last_vowel:
            return last_vowel[::-1]
    return ""
