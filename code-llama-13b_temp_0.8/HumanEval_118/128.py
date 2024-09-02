
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
    word = word[::-1]
    c_count = 0
    found = False

    for i, w in enumerate(word):
        if w in vowels:
            c_count = 0
            found = True
            continue
        c_count += 1
        if c_count == 2 and found:
            return w
    return ""

