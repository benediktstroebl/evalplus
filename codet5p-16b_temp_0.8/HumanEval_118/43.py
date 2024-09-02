
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

    last_consonant = 'Z'
    for idx, letter in enumerate(word):
        if letter not in 'aeiouAEIOU':
            continue
        if letter in 'AEIOU':
            if last_consonant not in 'AEIOU':
                return letter
            continue
        if last_consonant in 'aeiou':
            if letter not in 'aeiou':
                return letter
        last_consonant = letter
    return ''
