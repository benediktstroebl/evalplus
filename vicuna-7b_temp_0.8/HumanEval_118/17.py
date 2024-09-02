
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
    if len(word) < 2:
        return ""
    if word[0] == word[-1] and word[0] in "aeiouAEIOU":
        return word[0]
    else:
        start = 1
        for i in range(1, len(word)):
            if word[i] == word[i+1] and word[i] in "bcdfhjklmnpqrstvwxyz":
                end = i
                break
        if start == end:
            return ""
        return word[start:end+1]
