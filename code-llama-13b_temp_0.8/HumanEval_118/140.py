
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
    vowel = ['a', 'e', 'i', 'o', 'u']
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    reverse = word[::-1]
    if len(word) == 1:
        return ""
    elif len(word) == 2:
        for i in range(len(word)):
            if reverse[i] not in vowel:
                return ""
            else:
                return reverse[i]
    elif len(word) > 2:
        for i in range(len(word)-1):
            if reverse[i] in vowel and reverse[i+1] in consonant:
                return reverse[i]
            if reverse[i] in consonant and reverse[i+1] in consonant:
                return reverse[i]
        else:
            return ""
