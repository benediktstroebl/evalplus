
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
    vowels = {'a':'u', 'e':'i', 'i':'o', 'o':'a', 'u':'e'}

    idx = len(word) - 1
    while idx >= 0:
        if word[idx] not in vowels:
            idx -= 1
        else:
            return vowels[word[idx]]
    return ''

