
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
    if not word:
        return ''

    idx = 0
    while word[idx] in 'aeiou':
        idx += 1
    if word[idx] != 'y':
        return ''
    idx += 1
    while word[idx] in 'aeiou':
        idx += 1

    return word[idx]

