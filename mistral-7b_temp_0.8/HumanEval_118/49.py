
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
    vowel = "aeiou"
    consonant = "bcdfghjklmnpqrstvwxyz"
    # Your code goes here
    words = []
    for i in word:
        if i not in consonant and i in vowel:
            words.append(i)
    if len(words) != 0:
        return words[0]
    else:
        return ""

