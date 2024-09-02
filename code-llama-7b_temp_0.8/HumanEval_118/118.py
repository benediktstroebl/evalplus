
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
    vowels = ['A', 'E', 'I', 'O', 'U']
    if len(word) < 2:
        return ""
    i = len(word) - 1
    while word[i] in vowels:
        i -= 1
    j = i - 1
    while j >= 0:
        if word[j] in vowels:
            return word[j]
        j -= 1
    return ""

