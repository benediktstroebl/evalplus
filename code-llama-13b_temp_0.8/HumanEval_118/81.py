
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
    if len(word) == 0:
        return ""

    vowels = ["a", "e", "i", "o", "u"]

    # last 2 chars are vowels, no solution
    # word[-2] is vowel
    # word[-1] is not vowel
    if word[-2] in vowels and word[-1] not in vowels:
        return ""

    i = len(word) - 1
    while word[i] not in vowels and i > 0:
        i -= 1

    if i == 0:
        return ""

    return word[i]

