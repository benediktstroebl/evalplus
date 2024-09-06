
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

    last_vowel_idx = None
    consonant_count = 0

    for idx, letter in enumerate(word):
        if letter in ['a', 'e', 'i', 'o', 'u']:
            last_vowel_idx = idx
        elif letter not in ['a', 'e', 'i', 'o', 'u']:
            consonant_count += 1
    
    if last_vowel_idx == None or consonant_count == 0:
        return ''
    else:
        return word[last_vowel_idx]

    return ''

