
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
    vowels = {'a': 'e', 'e': 'a', 'i': 'o', 'o': 'i', 'u': 'a'}
    n = len(word)
    last_consonant = word[n-1]
    if last_consonant in vowels:
        return ""

    def helper(s, c, v):
        if v == "":
            return s
    
        if s == "":
            return v
        
        if s[0] in vowels and s[0] != c:
            return s[0] + helper(s[1:], c, v)
        elif s[0] == c:
            return helper(s[1:], c, v)     
        else:
            return s[0] + helper(s[1:], c, v)
    
    return helper(word[n-2:0:-1], last_consonant, "")

