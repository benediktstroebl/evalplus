
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
    vowels = "aeiou"
    for i in range(len(word)-1, -1, -1):
        if word[i] not in vowels:
            continue
        if word[i-1] not in vowels:
            continue
        if word[i]!= word[i-1]:
            continue
        closest_vowel = word[i]
        break
    return closest_vowel
