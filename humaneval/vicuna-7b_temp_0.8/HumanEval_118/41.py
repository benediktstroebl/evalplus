
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
    for i in range(1, len(word)):
        if word[i] in "bcdfghjklmnpqrstvwxyz":
            start = i - 1
            while word[start] in "bcdfghjklmnpqrstvwxyz":
                start -= 1
            end = i + 1
            while word[end] in "bcdfghjklmnpqrstvwxyz":
                end += 1
            if end - start > 1:
                return word[start:end]
    return ""

