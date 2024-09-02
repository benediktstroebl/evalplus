
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
    if len(word) <= 0:
        return ''
    if word[0] not in 'aeiouAEIOU':
        return word[0]
    if word[-1] not in 'aeiouAEIOU':
        return word[-1]
    return ''.join(set(word[1:]) & set(word[:-1]))
