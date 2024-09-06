
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

    i = len(word)-1
    # case insensitive, here I can convert to lowercase and use lower() 
    while i >= 0 and not word[i].isalpha():
        i -= 1

    if i == -1:
        return ""
    while i >= 0 and not word[i].isalpha():
        i -= 1

    if i == -1:
        return ""

    for j in range(i+1, len(word)):
        if word[j].lower() in "aeiou":
            return word[j]
    return ""

