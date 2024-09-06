
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
    if not word:
        return ""
    s = list(word)
    vowels = ['a','e','i','o','u']
    last_index = len(s)-1
    for i in range(len(s)-1,0,-1):
        if s[i] in vowels:
            last_index = i
            break
    s = s[last_index:]
    s.reverse()
    return ''.join(s)
