
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
    vowels = ["a", "e", "i", "o", "u"]
    consonants = ["q", "w", "r", "t", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
    word = list(word)
    length = len(word)
    if length <= 1 or word[-1] in vowels:
        return ""
    elif length == 2 or word[0] in vowels or word[-1] in vowels:
        return word[-2]
    else:
        for i in range(length-1, -1, -1):
            if word[i] in vowels:
                for j in range(length-1, i, -1):
                    if word[j] in vowels or word[j] in consonants:
                        return word[j]
    return ""

