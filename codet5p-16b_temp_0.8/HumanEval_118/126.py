
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

    left_vowels = set("aeiou")
    right_vowels = set("aeiou")
    for i, char in enumerate(word):
        if char in left_vowels:
            left_vowels.remove(char)
        elif char in right_vowels:
            right_vowels.remove(char)
        else:
            continue
    
    if len(right_vowels) == 0:
        return ""

    min_distance = len(word)
    result = ""

    for char in word:
        if char in left_vowels:
            if min_distance > i:
                result = char
                min_distance = i
    return result
