
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

    word = word.upper()
    n = len(word)
    if n == 0:
        return ""
    if n == 1:
        return word[0]
    
    for i in range(1, n-1):
        for j in range(i+1, n-1):
            if (word[i] in "BCDFGHJKLMNPQRSTVWXYZ" and word[j] in "BCDFGHJKLMNPQRSTVWXYZ") or (word[i] in "AEIOU" and word[j] in "aeiou"):
                continue
            if word[i] == word[j] and word[i] in "aeiou":
                return word[i]
    
    return ""
