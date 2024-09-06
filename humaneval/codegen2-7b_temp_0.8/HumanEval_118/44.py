
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
    l_consonant = [i for i in word if i not in string.ascii_lowercase]
    r_consonant = [i for i in word if i not in string.ascii_uppercase]
    r_vowel = [i for i in string.ascii_uppercase if i in string.ascii_lowercase]
    if r_consonant[-1] not in r_vowel:
        return ""
    return r_vowel[r_consonant.index(r_consonant[-1])-1]

