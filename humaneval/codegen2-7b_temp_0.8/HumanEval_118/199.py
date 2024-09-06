
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
    if len(word) == 0:
        return ""

    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    first_consonant = word[0]

    if first_consonant not in vowels:
        return ""

    for vowel in word:
        if vowel not in vowels:
            return vowel

    return ""

