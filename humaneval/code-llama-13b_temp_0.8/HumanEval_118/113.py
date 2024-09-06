
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
    # print(word)
    vowel = "aeiouAEIOU"
    for i, w in enumerate(word[::-1]):
        if i == 0:
            continue
        elif i == 1:
            if w in vowel and word[-1] not in vowel:
                return w
            else:
                return ""
        else:
            if word[-1] not in vowel and w in vowel:
                return w
            else:
                continue
    return ""
        
