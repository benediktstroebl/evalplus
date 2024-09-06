
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
    last_vowel = None
    for i in range(len(word)-1, 0, -1):
        if word[i] in 'aeiouAEIOU':
            last_vowel = word[i]
        if word[i] not in 'aeiouAEIOU' and word[i-1] not in 'aeiouAEIOU':
            return last_vowel
    return last_vowel

    # Another Approach
    # i = len(word)-1
    # while i > 0:
    #     if word[i] in 'aeiouAEIOU':
    #         while i > 0 and word[i-1] not in 'aeiouAEIOU':
    #             i -= 1
    #         return word[i]
    #     i -= 1
    # return ''
