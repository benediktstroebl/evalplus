
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
    ### edge cases: no vowels, one letter
    if len(word) < 3:
        return ""
    if "aeiouAEIOU" not in word:
        return ""
    ### nested loop, slow but easy to implement
    for i in range(len(word)-2,0,-1):
        if word[i] not in "aeiouAEIOU":
            for j in range(i-1,0,-1):
                if word[j] in "aeiouAEIOU":
                    return word[j]
    return ""
    
    #return ""
