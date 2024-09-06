
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
    vowels = "AEIOU"
    word_length = len(word)
    for i in range(word_length - 2, 0, -1):
        if word[i].isupper():
            if word[i+1].isupper() and word[i-1].islower():
                return word[i]
            elif word[i+1].isupper() and word[i-1].isupper():
                return ""
            elif word[i+1].isupper() and word[i-1].isupper():
                if word[i] in vowels:
                    return word[i]
                else:
                    return ""
            elif word[i+1].islower() and word[i-1].isupper():
                if word[i] in vowels:
                    return word[i]
                else:
                    return ""
            elif word[i+1].islower() and word[i-1].islower():
                if word[i] in vowels:
                    return word[i]
                else:
                    return ""
            elif word[i+1].islower() and word[i-1].isupper():
                return ""
    return ""
