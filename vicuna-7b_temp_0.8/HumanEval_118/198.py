
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
    word = word.lower()
    vowels = "aeiou"
    if not word:
        return ""
    n = len(word)
    for i in range(n-1):
        if word[i] in vowels:
            if word[i+1] == word[i+2]:
                v = word[i]
                break
            elif word[i+1] in vowels:
                v = word[i+1]
                break
            else:
                v = ""
        else:
            v = ""
    return v

