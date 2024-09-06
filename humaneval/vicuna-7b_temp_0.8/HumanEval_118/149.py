
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
    word = word.lower()
    left_index = word.find("c")
    if left_index == -1:
        return ""
    right_index = word.rfind("c")
    if right_index == -1:
        return ""
    if right_index < left_index:
        return ""
    for i in range(left_index + 1, right_index + 1):
        if word[i] in "aeiouAEIOU":
            return word[i]
    return ""
