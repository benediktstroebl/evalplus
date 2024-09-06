
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
    vowels = "aeiou"
    letters = list(word)

    vowel_index = 0
    i = len(letters) - 2
    while i > -1:
        if letters[i] in vowels:
            vowel_index = i
            break
        i -= 1

    j = len(letters) - 1
    while j > i:
        if letters[j] in vowels:
            return letters[j]
        j -= 1

    return ""

