
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
    right_half = word[::]
    i = len(right_half)
    while i > 0:
        for j in range(i-1, 0, -1):
            if not right_half[j].isalpha() and right_half[j] == right_half[i]:
                i = j
                break
        if i > 0:
            if right_half[i-1].isalpha() and right_half[i-1] == right_half[i].upper():
                return right_half[i-1]
    return ""
