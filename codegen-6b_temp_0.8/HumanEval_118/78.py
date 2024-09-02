
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
    vowels = "aeiou"
    word = list(word)
    if len(word) == 0: return ""
    if word[0] in vowels: return word[0]
    if word[-1] in vowels: return word[-1]
    
    if word[-1] == "F" or word[-1] == "f":
        word[-1] = "f"
        return "".join(word[:-1])
    
    if word[-2] == "F" or word[-2] == "f":
        word[-2] = "f"
        return "".join(word[:-1])
    
    for i in range(len(word)-3, -1, -1):
        if word[i] in vowels:
            word[i] = "f"
            return "".join(word)
    return ""
