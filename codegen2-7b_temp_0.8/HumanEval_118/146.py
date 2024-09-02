
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
    
    start = -1
    end = -1
    
    for i in range(len(word)):
        if word[i] not in VOWELS:
            start = i
            break
    
    for i in range(len(word) - 1, -1, -1):
        if word[i] not in VOWELS:
            end = i
            break
    
    if start!= -1 and end!= -1:
        return word[end + 1 : start]
    else:
        
