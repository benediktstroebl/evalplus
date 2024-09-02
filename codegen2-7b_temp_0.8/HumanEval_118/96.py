
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
    vowels = "aeiou"
    if len(word) == 1:
        return ""

    left_index = word.find("q")
    right_index = word.find("u")
    left_index = left_index if left_index >= 0 else len(word)
    right_index = right_index if right_index >= 0 else len(word)

    if left_index == right_index:
        return ""
    return word[right_index] if word[right_index] in vowels else word[left_index]

