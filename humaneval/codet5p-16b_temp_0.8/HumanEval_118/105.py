
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

    left_idx = -1
    right_idx = -1
    for i in range(len(word)):
        if word[i] in 'aeiou':
            left_idx = i
        if word[~i] in 'aeiou':
            right_idx = ~i
        if left_idx > -1 and right_idx > -1:
            break

    if left_idx < right_idx:
        return word[left_idx+1]
    return ""
        
        
        
