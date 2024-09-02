
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
    s = list(word)
    
    if s[0].lower() in ["a", "e", "i", "o", "u"]:
        return s[0].lower()
    
    # from right to left, find the first vowel
    for i in range(1, len(s)):
        if s[i].lower() in ["a", "e", "i", "o", "u"]:
            s[i-1] = s[i-1]+s[i]
            s.pop(i)
            break
    
    # from left to right, find the last vowel within the window
    for i in range(len(s)-2, -1, -1):
        if s[i].lower() in ["a", "e", "i", "o", "u"]:
            s[i] = s[i+1]+s[i]
            s.pop(i+1)
            break
    
    return "".join(s)
        
    