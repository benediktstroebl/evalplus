
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
    if 'a' in word and 'a' not in 'yqu':
        return 'a'
    elif 'e' in word and 'e' not in 'yqu':
        return 'e'
    elif 'i' in word and 'i' not in 'yqu':
        return 'i'
    elif 'o' in word and 'o' not in 'yqu':
        return 'o'
    elif 'u' in word and 'u' not in 'yqu':
        return 'u'
    else:
        return ''
