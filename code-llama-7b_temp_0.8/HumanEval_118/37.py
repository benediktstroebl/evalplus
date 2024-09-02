
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
    # [::-1] reverses the string
    vowels = set("aeiouAEIOU")
    # Remove all vowels from the string and count the remaining characters
    count = sum([1 for c in word[::-1] if c.lower() not in vowels])
    
    if count < 2:
        return ""
    
    for idx in range(len(word)):
        if word[idx].lower() in vowels:
            if word[idx].isupper():
                if idx+2 < len(word) and word[idx+2].lower() in vowels:
                    return word[idx+2]
                else:
                    return word[idx]
            else:
                if idx+1 < len(word) and word[idx+1].lower() in vowels:
                    return word[idx+1]
                else:
                    return word[idx]
    
    return ""
