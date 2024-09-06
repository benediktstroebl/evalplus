
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
    # First remove all vowels
    vowels = 'aeiouAEIOU'
    for vowel in vowels:
        word = word.replace(vowel, '')
    # print(word)
    
    # Then find the last char
    # Note that this will work for English letters only.
    # This is OK because we are given a string with English letters only.
    last_char = word[-1]
    
    # Then find the char before the last char
    last_but_one_char = word[-2]
    # print(last_but_one_char)
    
    # And check if last_char and last_but_one_char are consonants
    if last_but_one_char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and last_char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        return last_but_one_char
    
    # If both last_char and last_but_one_char are not consonants, return empty string
    return ''

