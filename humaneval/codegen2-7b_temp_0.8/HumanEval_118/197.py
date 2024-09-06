
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
    if not word:
        return ""
    c1 = word[0]
    for i in range(1, len(word)):
        if not word[i].isalpha():
            return ""
        if word[i] in "aeiou":
            return ""
        if word[i] in "AEIOU":
            return ""
        if word[i] == c1 and word[i] not in "AEIOU":
            c1 = word[i]
        elif word[i] == c1 and word[i] in "aeiou":
            return word[i]
    return
