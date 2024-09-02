
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    closest_vowel = ''
    start_i = None
    for i, char in enumerate(word[::-1]):
        if char in vowels:
            if not start_i:
                start_i = i
        else:
            if start_i:
                break
    
    if start_i:
        for vowel in vowels:
            if vowel in word[-start_i:]:
                closest_vowel = vowel
                break
        
    return closest_vowel

