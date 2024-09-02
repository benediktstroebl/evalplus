
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
    x = 0
    while x < len(word) - 1:
        if word[x] == word[x + 1] == "u" or word[x] == word[x + 1] == "U":
            return "U"
        if word[x] == word[x + 1] == "o" or word[x] == word[x + 1] == "O":
            return "O"
        if word[x] == word[x + 1] == "i" or word[x] == word[x + 1] == "I":
            return "I"
        if word[x] == word[x + 1] == "a" or word[x] == word[x + 1] == "A":
            return "A"
        if word[x] == word[x + 1] == "e" or word[x] == word[x + 1] == "E":
            return "E"
        x += 1
    return ""
