
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
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']
    if not word:
        return ""
    elif word[0] in vowel_list and word[-1] in vowel_list:
        return word[-1]
    elif word[0] not in vowel_list:
        return word[0]
    elif word[-1] not in vowel_list:
        return word[-1]
    else:
        return get_closest_vowel(word[1:-1])
