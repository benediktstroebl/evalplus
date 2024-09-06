
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
    def isVowel(ch):
        return ch in "aeiouAEIOU"
    vowel = ''
    idx = -1
    isFindVowel = False
    for i in range(len(word)-2, -1, -1):
        if isVowel(word[i]):
            if isFindVowel:
                idx = i
                break
            vowel = word[i]
            isFindVowel = True
        else:
            isFindVowel = False
    if idx == -1:
        return vowel
    for i in range(idx, -1, -1):
        if not isVowel(word[i]):
            idx = i
            break
    return word[idx+1]
