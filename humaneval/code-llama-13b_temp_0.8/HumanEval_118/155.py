
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
    if len(word) < 3:
        return ""
    
    last_vowel = ""
    last_consonant = ""
    
    for i in range(len(word) - 1, 0, -1):
        if word[i] in "aeiouAEIOU":
            if last_consonant != "":
                return last_vowel
            
            last_vowel = word[i]
            
        else:
            last_consonant = word[i]
    
    return ""
