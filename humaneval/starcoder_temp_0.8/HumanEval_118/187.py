
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
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    vowels = [item.lower() for item in vowels]
    if len(word) <= 3:
        return ""
    for i in range(len(word)):
        if word[i] in vowels:
            if i == 0:
                if word[1] not in vowels:
                    return word[1]
                if word[2] not in vowels:
                    return word[2]
            if i == (len(word) - 1):
                if word[i-1] not in vowels:
                    return word[i-1]
            if i > 0 and i < (len(word) - 1):
                if word[i-1] not in vowels:
                    return word[i-1]
                if word[i+1] not in vowels:
                    return word[i+1]
