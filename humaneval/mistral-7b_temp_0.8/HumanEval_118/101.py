
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
    if word == word.upper():
        word = word.lower()

    if word[0] in "aeiouAEIOU":
        word = word[1:]
    elif word[-1] in "aeiouAEIOU":
        word = word[:-1]

    if word == "":
        return ""

    for i in range(len(word)):
        if word[i] in "aeiouAEIOU" and word[i - 1] not in "aeiouAEIOU" and word[i + 1] not in "aeiouAEIOU":
            return word[i]


