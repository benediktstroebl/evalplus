
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
    start = -1
    end = -1
    for i in range(len(word)):
        if word[i].isupper():
            if start == -1:
                start = i
            end = i
        elif word[i].islower():
            end = i
    return "" if start == -1 or end == -1 else word[start:end+1]

