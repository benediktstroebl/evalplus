
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
    if len(word) < 1:
        return ''
    if word[0] in ('a', 'e', 'i', 'o', 'u'):
        return word[0]
    # checking for consonant
    for i, v in enumerate(reversed(word), 1):
        if not v.isalpha():
            continue
        if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u':
            return word[len(word)-i:]
    return ''
