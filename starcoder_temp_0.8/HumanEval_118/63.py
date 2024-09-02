
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
    vowels = "aeiouyAEIOUY"
    if len(word) < 3:
        return ""

    # Check if the last character is a vowel, if not, keep going until it is
    while word[-1] not in vowels:
        if len(word) < 3:
            return ""
        word = word[:-1]

    # Check if the second last character is a vowel, if not, keep going until it is
    while word[-2] not in vowels:
        word = word[:-1]

    # Return the vowel we found, if none, return empty string
    if len(word) == 0:
        return ""
    else:
        return word[-1]

