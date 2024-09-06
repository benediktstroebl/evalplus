
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
    left_index = len(word) - 1
    right_index = 0
    
    while right_index < len(word) and word[right_index] == word[left_index] + 1:
        right_index += 1
    
    if right_index >= len(word):
        return ""
    
    middle_index = right_index + (len(word) - right_index) // 2
    vowels = ["a", "e", "i", "o", "u"]
    
    for i, c in enumerate(word[middle_index:]):
        if c in vowels:
            return vowels[i]
    
    return ""
