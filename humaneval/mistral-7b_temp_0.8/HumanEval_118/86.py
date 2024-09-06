
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
    letters = list(word)

    for i in range(len(letters) - 1):
        if letters[i].lower() in "aeiou":
            if i == 0:
                continue
            elif letters[i - 1].isalpha() and not letters[i - 1].islower() and letters[i + 1].isalpha() and not letters[i + 1].islower():
                return letters[i]

    return ""




