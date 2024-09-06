
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
    # find the first consonant
    first_cons = -1
    for i in range(len(word)-1, 0, -1):
        if word[i].isupper():
            first_cons = i
            break
    if first_cons == -1:
        return ""
    # find the last consonant
    last_cons = -1
    for i in range(len(word)-1, first_cons-1, -1):
        if word[i].isupper():
            last_cons = i
            break
    if last_cons == -1:
        return ""
    # find the closest vowel
    closest_vowel = ""
    for i in range(last_cons, first_cons-1, -1):
        if word[i].lower() in "aeiouy":
            closest_vowel = word[i]
            break
    return closest_vowel

