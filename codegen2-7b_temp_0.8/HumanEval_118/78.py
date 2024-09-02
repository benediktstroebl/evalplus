
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
    vowels = ['a','e','i','o','u']
    
    l = 0
    r = len(word)-1
    while l<r:
        if word[l] in vowels and word[r] in vowels:
            l += 1
            r -= 1
        elif word[l] in vowels:
            l += 1
        elif word[r] in vowels:
            r -= 1
        else:
            return ""
    return word[l]
    
