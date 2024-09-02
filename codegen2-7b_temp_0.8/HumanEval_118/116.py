
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
    vowels = "aeiouAEIOU"
    closest_vowel = ""
    for char in word:
        for vowel in vowels:
            if char in vowels:
                if len(closest_vowel) == 0:
                    closest_vowel = char
                if char == closest_vowel:
                    closest_vowel = char
    if len(closest_vowel) == 0:
        return ""
    return closest_vowel
    
    
