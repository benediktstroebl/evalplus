
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
    if word == "":
        return ""
    start = 0
    for i in range(len(word)):
        if word[i] == "":
            start = i
            break
    end = len(word)
    for i in range(start, end):
        if word[i] == "s" or word[i] == "t" or word[i] == "f" or word[i] == "h" or word[i] == "v" or word[i] == "g":
            continue
        if word[i] == "r":
            if word[i+1] == "d":
                return word[i+2]
            if word[i+1] == "b":
                return word[i+2]
            if word[i+1] == "s":
                return word[i+2]
            if word[i+1] == "m":
                return word[i+2]
            if word[i+1] == "p":
                return word[i+2]
    return ""
