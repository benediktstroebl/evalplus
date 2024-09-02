
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
    # special case
    vowels = "aeiou"
    word = word.lower()
    if word == "":
        return ""
    if len(word) == 1:
        return ""
    if len(word) == 2:
        if word[1] in vowels:
            return word[1]
        else:
            return ""

    for i in range(len(word)-2, -1, -1):
        if word[i] in vowels:
            if word[i+1] not in vowels:
                if word[i+2] in vowels:
                    return word[i]
                else:
                    return ""
            else:
                return ""



