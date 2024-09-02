
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
    right_index = len(word) - 1
    while right_index > 0:
        if word[right_index] in VOWELS:
            right_index -= 1
        elif word[right_index] not in VOWELS:
            right_index -= 1
            while right_index > 0:
                if word[right_index] in VOWELS:
                    return word[right_index]
                right_index -= 1
            return ""
    return ""
