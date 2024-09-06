
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
    vowel_to_char = {"a": "A", "e": "E", "i": "I", "o": "O", "u": "U", "y": "Y"}
    vowels = set(vowel_to_char.values())
    return_vowel = ""
    for index, letter in enumerate(word[::-1]):
        if letter in vowels and word[-index-1] in vowels:
            return_vowel = vowel_to_char[word[-index-1]]
    return return_vow
