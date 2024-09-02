
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
    
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    right_most_consonants = ""
    
    for letter in reversed(word):
        if letter not in vowels:
            right_most_consonants += letter
        else:
            break
    if right_most_consonants:
        for vowel in reversed(right_most_consonants):
            if vowel in vowels:
                return vowel
    return ""
