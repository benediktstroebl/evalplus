
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
    if len(word) < 2:
        return ""
    start = 0
    end = 1
    while end < len(word) - 1:
        if word[end] in "bcdfghjklmnpqrstvwxyz":
            end += 1
        elif word[end] in "aeiou":
            end += 1
        else:
            break
    while start < end:
        if word[start] in "bcdfghjklmnpqrstvwxyz":
            start += 1
        else:
            break
    return word[start:end]
