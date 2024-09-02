
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

    i = 0
    while i < len(word) - 1:
        if word[i].upper() in "AEIOU" and word[i + 1].upper() in "AEIOU" and word[i - 1].upper() not in "AEIOU":
            return word[i].upper()
        elif word[i].upper() in "AEIOU" and word[i + 1].upper() not in "AEIOU" and word[i - 1].upper() in "AEIOU":
            return word[i].upper()
        elif word[i].upper() not in "AEIOU" and word[i + 1].upper() in "AEIOU" and word[i - 1].upper() not in "AEIOU":
            return word[i + 1].upper()
        i += 1
    return ""
