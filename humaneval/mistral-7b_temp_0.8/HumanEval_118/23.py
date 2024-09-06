
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
    # empty string
    vowel = ""
    # find first consonant
    if word[1] in "aeiouAEIOU":
        # get index
        i = word.find(word[1])
        # check for next consonant
        if word[i+2] in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            vowel = word[i+2]
        # check for previous consonant
        elif word[i-2] in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            vowel = word[i-2]
    # find last consonant
    if word[-2] in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        # get index
        i = word.rfind(word[-2])
        # check for next consonant
        if word[i
