
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

    
    vowels = ["a", "e", "i", "o", "u"]
    closest_vowel = ""
    
    if len(word) < 3:
        return closest_vowel
    
    for index in range(len(word)-2, -1, -1):
        if word[index] == word[index+1]:
            continue
        
        if word[index] in vowels and word[index+1] not in vowels:
            closest_vowel = word[index]
            break
    
    return closest_vowel
