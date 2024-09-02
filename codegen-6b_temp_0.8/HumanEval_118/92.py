
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
    
    # if the word only consists of vowels
    if word.isalpha():
        return ""
    # if the word is blank
    elif not word:
        return ""
    
    vowels = "aeiou"

    # return the last vowel that is not in the beginning or the end of the word
    for i in range(len(word) - 1, 0, -1):
        if word[i] in vowels:
            return word[i]
    
    # return the last consonant in the word
    return word[-1]
