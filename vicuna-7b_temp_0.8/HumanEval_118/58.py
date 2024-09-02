
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
    n = len(word)
    if n == 1 or n == 2:
        return ""
    # sort word in alphabetical order
    word = sorted(word)
    # get the indices of consonants
    c1 = word.find("c") + 1
    c2 = word.rfind("c")
    # check if there is any vowel in between
    v1 = word.find("v")
    if v1 != -1 and v1 < c1:
        return word[v1:c1]
    v2 = word.rfind("v")
    if v2 != -1 and v2 > c2:
        return word[v2:c2]
    return ""
