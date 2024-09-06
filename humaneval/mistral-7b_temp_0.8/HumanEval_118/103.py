
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
    def is_vowel(ch):
        return ch.lower() in "aeiouy"

    def is_consonant(ch):
        return ch.lower() not in "aeiouy"

    chars = list(word)
    i = 0
    while True:
        if is_vowel(chars[i]):
            return chars[i]
        i += 1
        if i == len(chars) - 1:
            return ""

        if is_consonant(chars[i]) and is_consonant(chars[i + 1]):
            return chars[i + 1]
        i += 2

