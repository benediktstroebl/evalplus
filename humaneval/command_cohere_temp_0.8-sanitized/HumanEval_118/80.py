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
    # Using find_all to find indices of all occurrences of consonants and vowels
    consonants = [m.start() for m in word.find_all('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ', windy=False)]
    vowels = [m.start() for m in word.find_all('aeiouAEIOU', windy=False)]
    
    # Checking if any match with the condition and return the closest one
    for vowel in vowels:
        if len(consonants) >= 2 and consonants[-2] < vowel < consonants[-1]:
            return word[vowel]
    return ""