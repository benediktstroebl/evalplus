
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
    if len(word) <= 2:
        return ""
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    temp = word[::-1]
    index = len(temp)
    for i in range(len(temp)):
        if temp[i] in vowels:
            if (index - i) >= 2:
                if temp[i+1] not in vowels:
                    return temp[i]
            else:
                return temp[i]
        index -= 1
    return ""

