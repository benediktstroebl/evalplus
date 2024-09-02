
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
    vowels = 'aeiouAEIOU'
    word = list(word)
    c1 = ""
    c2 = ""
    v = ""
    for i in range(len(word)):
        if word[i].lower() in vowels:
            v = word[i].lower()
        elif word[i] in vowels:
            c2 = word[i]
        else:
            c1 = word[i]
    if c1 == "" or c2 == "":
        return ""
    else:
        return v
