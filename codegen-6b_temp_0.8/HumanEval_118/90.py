
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
    if word == "":
        return word
    
    is_vowel = lambda x: x in ["a", "e", "i", "o", "u"]
    words = list(word)
    
    i = len(words)-1
    
    while i > 0:
        if is_vowel(words[i]):
            return words[i]
        i -= 1
    
    return ""
