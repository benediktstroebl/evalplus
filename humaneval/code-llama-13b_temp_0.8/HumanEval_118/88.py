
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
    consonants = "bcdfghjklmnpqrstvwxyz"
    c = set(consonants)
    v = set(vowels)
    r = word[::-1]
    for i in range(len(r)):
        if r[i] in c and i < len(r) - 1 and r[i+1] in v:
            return r[i+1]
    return ""
