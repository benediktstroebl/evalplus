
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
    last_vowel_index = None
    for i, char in enumerate(word):
        if char in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
            last_vowel_index = i
    
    if last_vowel_index == None or last_vowel_index == 0 or last_vowel_index == len(word) - 1:
        return ""

    for i in range(last_vowel_index + 1, len(word)):
        if word[i] not in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
            return word[i]
    return ""
