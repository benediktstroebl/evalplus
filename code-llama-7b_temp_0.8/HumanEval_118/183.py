
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
    vowel = "AEIOU"
    for i in range(len(word)-1, -1, -1):
        if word[i].upper() in vowel:
            if i == 0:
                return ""
            elif (word[i-1] in vowel) or (i+1 == len(word)):
                return word[i]
    return ""
