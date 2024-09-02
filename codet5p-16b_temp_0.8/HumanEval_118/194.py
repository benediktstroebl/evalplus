
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
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    
    closest_vowel = ""
    
    for i, c in enumerate(word):
        if c not in consonants:
            continue
        if c in vowels:
            closest_vowel = c
            break
        elif c in consonants:
            vowel_index = len(word) - 1 - i
            vowel = ""
            while vowel not in vowels and vowel_index > 0:
                vowel = word[vowel_index]
                vowel_index -= 1
            if vowel in vowels:
                closest_vowel = vowel
                break
    return closest_vowel


    
    
