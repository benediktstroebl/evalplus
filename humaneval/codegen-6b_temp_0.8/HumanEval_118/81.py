
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
    vowels = {'a', 'e', 'i', 'o', 'u'}
    n = len(word)
    if n == 0 or not word.isalpha():
        return ""
    curr_vowel = ""
    for i in range(n-1, -1, -1):
        if word[i] not in vowels:
            if curr_vowel != "":
                return curr_vowel
        else:
            curr_vowel = word[i]
    return ""
