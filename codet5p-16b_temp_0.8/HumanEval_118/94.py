
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

    
    result = ''
    for i,char in enumerate(word):
        if char in "aeiou":
            return char
        elif char in "bcdfgjklmnpqrstvwxyz":
            for j,char2 in enumerate(word[i:]):
                if char2 in "aeiou":
                    return char2
                    break
                elif char2 in "bcdfgjklmnpqrstvwxyz":
                    continue
                else:
                    return result
                    break
    return result

