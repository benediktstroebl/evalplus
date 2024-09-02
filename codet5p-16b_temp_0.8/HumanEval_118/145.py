
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

    if not word:
        return ""
    vowels = "aeiou"
    for index, char in enumerate(word):
        if char in vowels:
            return char
        if char == "y" and word[index+1] in vowels:
            return "y"
        if char == "z" and word[index+1] in vowels:
            return "z"
        if char == "x" and word[index+1] in vowels:
            return "x"
    return ""
