
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
    # YOUR CODE HERE
    if word.count("A") > 0:
        return "A"
    if word.count("E") > 0:
        return "E"
    if word.count("I") > 0:
        return "I"
    if word.count("O") > 0:
        return "O"
    if word.count("U") > 0:
        return "U"

    return ""
