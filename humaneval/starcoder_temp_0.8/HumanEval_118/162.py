
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
    vowels = ["a", "e", "i", "o", "u"]
    vowel_index = -1
    min_index = len(word)

    for char_index, char in enumerate(word):
        if char in vowels:
            if char_index >= 1 and char_index < len(word) - 1:
                min_index = min(min_index, char_index)

    if min_index == len(word):
        return ""
    else:
        return word[min_index]
