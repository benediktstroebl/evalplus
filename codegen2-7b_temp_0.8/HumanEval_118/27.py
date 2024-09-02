
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
    result = ""
    for char in word:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            return result
        elif char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
            result += char
        else:
            result = ""
            break
    return result
