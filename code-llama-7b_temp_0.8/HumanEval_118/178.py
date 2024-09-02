
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
    if len(word) < 3:
        return ""
    
    index = len(word) - 1
    
    while word[index].islower():
        index -= 1
        if index < 0:
            return ""
    
    while not word[index].islower():
        if word[index] in "aeiou":
            return word[index]
        index -= 1
        if index < 0:
            return ""
    
    while word[index].isupper():
        index -= 1
        if index < 0:
            return ""
    
    while not word[index].isupper():
        if word[index] in "AEIOU":
            return word[index]
        index -= 1
        if index < 0:
            return ""
    
    return ""

