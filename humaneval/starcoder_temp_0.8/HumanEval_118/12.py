
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
    i, j = len(word) - 2, len(word) - 1
    while i >= 0 and j <= len(word) - 1:
        if word[i] not in "aeiou":
            i -= 1
            continue
        elif word[j] not in "aeiou":
            j += 1
            continue
        else:
            return word[i]
    return ""

