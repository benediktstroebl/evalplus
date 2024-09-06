
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
    word = word.lower()
    if len(word) < 3:
        return ""
    c1 = word[0]
    if not c1 in vowels:
        return ""
    c2 = word[-1]
    if not c2 in vowels:
        return ""
    for c in word[1:-1]:
        if c in vowels:
            return c
    return ""
