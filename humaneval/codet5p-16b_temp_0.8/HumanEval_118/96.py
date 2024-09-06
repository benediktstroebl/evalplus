
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

    
    prev = None
    current = None
    for i in range(len(word) - 1, -1, -1):
        if word[i].lower() in "aeiou":
            current = word[i]
            break
        prev = word[i]
    
    if prev.lower() in "aeiou" and not current:
        return ""
    
    result = ""
    while prev.lower() not in "aeiou" and prev and prev!= current:
        result = prev
        prev = prev[:-1]

    if prev == current:
        result = current
    else:
        result = prev
        
    return result

