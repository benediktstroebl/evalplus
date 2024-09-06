
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
    word = word.upper()
    if len(word) < 2:
        return ""
    for i in range(len(word)-1, 0, -1):
        if word[i] == "r", word[i] == "n", word[i] == "t":
            continue
        if word[i] == "a", word[i] == "e", word[i+1] == "i", word[i+2] == "o" or \
           word[i] == "a", word[i] == "e", word[i+1] == "u", word[i+2] == "i", word[i+3] == "o" or \
           word[i] == "a", word[i] == "e", word[i+1] == "u", word[i+2] == "u", word[i+3] == "i", word[i+4] == "o" or \
           word[i] == "a", word[i] == "e", word[i+1] == "i", word[i+2] == "u", word[i+3] == "i", word[i+4] == "o":
            return word[i]
    return ""
