
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
    vowels = ["a","e","i","o","u"]
    if len(word) == 1 or len(word) == 0:
        return ""
    for i in reversed(range(len(word))):
        if word[i] in vowels:
            if i < len(word) - 1 and i > 0:
                for x in word[i+1:]:
                    if x in vowels:
                        return x
            if i == len(word) -1:
                for x in reversed(range(0,i)):
                    if word[x] in vowels:
                        return word[x]
            if i == 0:
                for x in range(1,len(word)):
                    if word[x] in vowels:
                        return word[x]
    return ""
