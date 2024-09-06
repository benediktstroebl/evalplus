
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
    last_index = len(word) - 1
    first_index = 0
    for index in range(len(word)):
        if word[index] in vowels:
            first_index = index
            break
    for index in range(len(word) - 1, -1, -1):
        if word[index] in vowels:
            last_index = index
            break
    if last_index == 0 or first_index == last_index:
        return ""
    return word[last_index]
