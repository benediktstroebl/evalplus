
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
    if len(word) < 2:
        return ""
    right_half = word[1:]
    left_half = word[:-1]
    half_set = set(left_half)
    half_set.discard('a')
    half_set.discard('e')
    half_set.discard('i')
    half_set.discard('o')
    half_set.discard('u')
    for char in right_half:
        if char in half_set:
            return char
    return ""
