
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
    vowels = ['a','e','i','o','u']
    length = len(word)-1
    idx = length
    while idx >= 0:
        if word[idx].lower() in vowels:
            if idx < length - 1:
                for i in range(idx+1, length):
                    if word[i].lower() in vowels:
                        return word[i]
        idx -= 1
    return ""
    
