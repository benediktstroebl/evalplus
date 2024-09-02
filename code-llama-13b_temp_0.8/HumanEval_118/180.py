
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
    last_vowel = None
    next_vowel = None
    for i in range(len(word)-1, -1, -1):
        if word[i] in 'aeiouAEIOU':
            if last_vowel is None:
                next_vowel = word[i]
            break
        last_vowel = word[i]
    
    if next_vowel is not None:
        return next_vowel
    
    for i in range(len(word)):
        if word[i] in 'aeiouAEIOU':
            return word[i]
            
    return ""
