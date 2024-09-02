
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
    word = word.lower()
    if len(word) < 3:
        return ""
    elif word.startswith("y") and word.endswith("u"):
        return "u"
    elif word[1] in "aeiou" and word[-1] in "aeiou":
        return word[1]
    elif word[0] in "aeiou" and word[-2] in "aeiou":
        return word[-2]
    elif word[0] in "aeiou":
        return word[1]
    elif word[-1] in "aeiou":
        return word[-2]
    else:
        return ""
