
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
    vowel_list = ["a", "e", "i", "o", "u"]
    closest_vowel = ""
    if word == "":
        return closest_vowel
    if word[0] not in vowel_list:
        return closest_vowel
    if word[-1] not in vowel_list:
        return closest_vowel
    for vowel in word[1:-1]:
        if vowel in vowel_list:
            closest_vowel = vowel
    return closest_vowel
