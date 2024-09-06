
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

    if 'u' in word:
        return 'u'
    elif 'a' in word:
        return 'a'
    elif 'e' in word:
        return 'e'
    elif 'o' in word:
        return 'o'
    elif 'i' in word:
        return 'i'
    else:
        return ""

