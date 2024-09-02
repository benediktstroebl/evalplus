
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
    # First create a list to store the indexes of all the vowels
    vowels = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }

    # Iterate the string and add the vowel and their indexes to the vowels
    for index, letter in enumerate(word):
        if letter in vowels.keys():
            vowels[letter] = index

    # Check the last vowel
    if vowels["u"] > 0:
        return word[vowels["u"] - 1]
    else:
        # Check the last consonant
        for letter in word[::-1]:
            if letter in vowels.keys():
                return word[vowels[letter] + 1]
    
    return ""
