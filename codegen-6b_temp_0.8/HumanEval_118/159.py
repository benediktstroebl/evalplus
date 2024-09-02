
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
    chars = list(word)
    length = len(chars)
    index = length - 1
    vowels = ['a', 'e', 'i', 'o', 'u']
    while index > 0:
        if chars[index] not in vowels:
            index -= 1
        else:
            break
    index2 = len(chars) - 1
    while index2 > index:
        if chars[index2] not in vowels:
            index2 -= 1
        else:
            break
    return chars[index2] if index2 < index else ''
