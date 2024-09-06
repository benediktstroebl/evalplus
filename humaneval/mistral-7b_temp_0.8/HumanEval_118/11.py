
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
    vowels = "aeiouy"
    if len(word) == 0:
        return ""
    i = 0
    while word[i] not in vowels and i < len(word)-1:
        i += 1
    if i == len(word)-1:
        return ""
    while word[i+1] not in vowels and i < len(word)-2:
        i += 1
    if i == len(word)-2:
        return ""
    return word[i+1]

