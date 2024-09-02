
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
    vowels = ["a","e","i","o","u"]
    # iterate the word from right to left
    for i in range(len(word)-1,-1,-1):
        # if char at index i is a vowel
        if word[i].lower() in vowels:
            # if char at index i-1 is consonant
            if word[i-1].lower() not in vowels:
                return word[i]
    return ""
