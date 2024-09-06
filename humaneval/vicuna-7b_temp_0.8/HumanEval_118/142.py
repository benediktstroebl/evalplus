
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
    vowels = "aeiouAEIOU"
    word = word.lower()
    start = 0
    end = len(word) - 1
    
    while start <= end:
        if word[start] == "r" and word[end] == "r":
            start += 1
            end -= 1
            continue
        
        if word[start] == word[end] or (word[start] == "w" and word[end] == "w") or (word[start] == "h" and word[end] == "h"):
            start += 1
            end -= 1
            continue
        
        if word[start] in vowels:
            return word[start]
        
        start += 1
    
    return ""

