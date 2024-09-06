
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

    vowels = set("aeiou")
    consonants = set("bcdfghjklmnpqrstvwxyz")

    if not word[0].isalpha():
        return ""
    if not word[-1].isalpha():
        return ""

    word = word[::-1]
    for index, char in enumerate(word):
        if char in consonants:
            if word[index + 1: index + 2] in vowels:
                return word[index + 1: index + 2]
            return word[index: index + 2]
    return ""


