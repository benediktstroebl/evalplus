
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
    vowel = "aeiouAEIOU"
    consonant = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    if len(word) == 1:
        return ""
    elif word.count(' ') > 0:
        w = word.split()
        for x in w:
            if x.count(' ') > 0:
                continue
            else:
                for y in x:
                    if y in vowel:
                        return y
    else:
        for x in word:
            if x in vowel:
                if x in consonant + vowel + consonant:
                    return x
    return ""

