
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
    # l = len(word)
    # for i in range(l-1, 0, -1):
    #     if word[i].isalpha() and word[i].isupper():
    #         if word[i-1].isalpha() and word[i-1].islower():
    #             return word[i]
    # return ""
    
    vowels = "aeiouy"
    vowels_idx = []
    # get all vowels' index
    for i in range(len(word)):
        if word[i] in vowels:
            vowels_idx.append(i)
    if len(vowels_idx) < 2:
        return ""
    # get the closest vowels
    result = []
    for i in range(len(vowels_idx)-1):
        for j in range(i+1, len(vowels_idx)):
            if abs(vowels_idx[i] - vowels_idx[j]) == 1:
                result.append(word[vowels_idx[j]])
    return max(result, key=result.count)

