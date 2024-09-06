
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
    vowels = "AEIOU"
    cons = "QWERTYUIOPASDFGHJKLZXCVBNM"
    
    if len(word) == 0 or word[0] not in cons or word[-1] not in cons:
        return ""
    if word[0] in vowels:
        word = word[1:]
    if word[-1] in vowels:
        word = word[:-1]
    for i in range(len(word)):
        if word[i] in vowels and word[i-1] in cons and word[i+1] in cons:
            return word[i]
    return ""

