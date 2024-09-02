
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

    closest_vowel = ""
    for i in range(len(word)):
        if word[i] == "a":
            closest_vowel = "a"
            break
        elif word[i] == "e":
            closest_vowel = "e"
            break
        elif word[i] == "i":
            closest_vowel = "i"
            break
        elif word[i] == "o":
            closest_vowel = "o"
            break
        elif word[i] == "u":
            closest_vowel = "u"
            break
    for i in range(len(word)-1, 0, -1):
        if word[i] == "a":
            closest_vowel = "a"
            break
        elif word[i] == "e":
            closest_vowel = "e"
            break
        elif word[i] == "i":
            closest_vowel =
