
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
    max_dist = len(word)
    if len(word) == 0:
        return ""
    for i in range(1, len(word)):
        if word[len(word)-i] in "AEIOUaeiou":
            dist = i-1
            if dist < 0:
                dist = 0
            if abs(dist) < abs(max_dist):
                max_dist = dist
    if max_dist == len(word):
        return ""
    else:
        return word[max_dist]

