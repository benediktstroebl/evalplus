
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

    vowels = set(["a", "e", "i", "o", "u", "y"])
    index = len(word) - 1
    while index >= 0:
        if word[index] not in vowels:
            if index > 0 and word[index - 1] in vowels:
                return word[index]
            if index == 0 and word[index - 1] in vowels:
                return ""
        index -= 1
    return ""

