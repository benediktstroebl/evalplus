
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
    # Rules:
    # 1. If word is vowel, return itself
    # 2. If word is consonant, get the first vowel after it
    # 3. If there are no more consonants, return ""
    
    # edge cases:
    # 1. if word length is 1, return ""
    # 2. if there are no more consonants, return ""
    # 3. if word is vowel, return itself
    
    if len(word) == 1:
        return ""
    
    vowels = set("aeiouAEIOU")
    # print(word[-1])
    # print(word[1])
    # print(word[0])
    
    if word[-1] in vowels:
        return word[-1]
    if word[1] in vowels:
        return word[1]
    if word[0] in vowels:
        return word[0]
    
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels and word[i+1] not in vowels:
            return word[i]
        
    return ""


