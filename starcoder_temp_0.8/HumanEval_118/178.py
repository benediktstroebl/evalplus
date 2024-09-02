
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
    vowels = 'aeiou'
    left_side = []
    right_side = []
    for idx, c in enumerate(word):
        if c in vowels:
            left_side.append(c)
        else:
            right_side.append(c)

    right_side.reverse()

    if right_side:
        return right_side[0]
    else:
        return ''

