
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
    result = ""
    
    vowels = "aeiou"
    
    for idx in range(len(word)-2, 0, -1):
        if word[idx].lower() in vowels:
            if word[idx].lower() == word[idx]:
                result = word[idx]
            else:
                result = word[idx].lower()
            break
            
    return result
