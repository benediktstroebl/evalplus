
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
    vowels = "AEIOUaeiou"
    left_cons = ""
    right_cons = ""
    for i in word:
        if i in vowels:
            right_cons += i
        else:
            left_cons += i
    if not left_cons or not right_cons:
        return ""
    if right_cons in left_cons:
        return right_cons
    else:
        return left_cons

