
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
    # R1:
    vowels = ['A', 'E', 'I', 'O', 'U']
    if len(word) == 0: return ""
    if len(word) == 1: return ""

    # rightmost_vowel = vowels[-1]
    # rightmost_consonant = word[-1]
    # if rightmost_consonant in vowels:
    #     return rightmost_vowel
    # for i in range(len(word) - 2, -1, -1):
    #     if word[i] in vowels:
    #         return word[i]
    # return ""

    # R2:
    vowels = ['A', 'E', 'I', 'O', 'U']
    if len(word) == 0: return ""
    if len(word) == 1: return ""
    # rightmost_vowel = vowels[-1]
    # rightmost_consonant = word[-1]
    # if rightmost_consonant in vowels:
    #     return rightmost_vowel
    # for i in range(len(word) - 2, -1, -1):
    #     if word[i] in vowels:
    #         return word[i]
    # return ""

    # R3:
    vowels = ['A', 'E', 'I', 'O', 'U']
    if len(word) == 0: return ""
    if len(word) == 1: return ""
    rightmost_vowel = vowels[-1]
    rightmost_consonant = word[-1]
    if rightmost_consonant in vowels:
        return rightmost_vowel
    for i in range(len(word) - 2, -1, -1):
        if word[i] in vowels:
            return word[i]
    return ""

