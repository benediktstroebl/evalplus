
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
    # REPLACE THE RETURN STATEMENT WITH YOUR CODE
    cons = ""
    vowels = ["a","e","i","o","u"]
    count = 0
    for i in range(len(word)):
        if word[i] not in vowels:
            cons = word[i]
            count += 1
            if count > 1:
                break
    
    if count == 1:
        return ""
    
    if cons == "":
        return ""
    
    word = word.split("")
    for i in range(len(word)-1,-1,-1):
        if word[i][0] in vowels:
            return word[i]

    return ""
    
    