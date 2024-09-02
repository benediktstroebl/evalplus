
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
    vowels = list("AEIOU")
    for right in reversed(range(1, len(word) + 1)):
        if word[-right] not in vowels:
            continue
        for left in range(right - 1, -1, -1):
            if word[left] not in vowels:
                continue
            return word[-right + 1:][:left + 1]
    return ""
