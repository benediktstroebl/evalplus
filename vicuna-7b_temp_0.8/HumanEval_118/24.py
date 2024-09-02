
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
    if len(word) == 1:
        return ""
    left_half = word[:len(word)-1]
    right_half = word[len(word)-1:]
    left_half_vowels = find_vowels(left_half)
    for vowel in left_half_vowels:
        right_half_index = right_half.find(vowel, len(left_half_vowels[0]))
        if right_half_index != -1:
            return right_half[right_half_index+len(vowel):]
    return ""
