
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

    if len(word) < 3:
        return ''
    for i, char in enumerate(word):
        if char in ['a', 'e', 'i', 'o', 'u']:
            return char
        elif char in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l','m', 'n', 'p', 'q', 'r','s', 't', 'v', 'w', 'x', 'y', 'z']:
            if i < len(word)-2 and word[i+1] in ['a', 'e', 'i', 'o', 'u'] and word[i+2] in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l','m', 'n', 'p', 'q', 'r','s', 't', 'v', 'w', 'x', 'y', 'z']:
                return word[i+1]
            elif i == len(word)-2 and word[i+1] in ['b',
