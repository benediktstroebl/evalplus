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
    # Using a dictionary to detect the consonants for efficiency
    CONSONANTS = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')

    # Find if there is any vowel meet the condition
    vowels_count = 0
    for char in word:
        if char.isalpha() and char in CONSONANTS and (char.lower() in 'aeiouAEIOU'):
            vowels_count += 1
            if vowels_count == 2: return char
    return ""