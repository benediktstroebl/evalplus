
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

    vowels = "aeiouAEIOU"
    index = len(word) - 1

    # if string is empty return nothing
    if len(word) == 0:
        return ""
    
    # if string starts with consonant return nothing
    if word[0] not in vowels:
        while index > 0:
            if word[index] in vowels:
                return word[index]
            index -= 1
    # if string starts with vowel return the next vowel
    else:
        while index > 0:
            if word[index] in vowels:
                if word[index - 1] not in vowels:
                    return word[index]
            index -= 1
    return ""
