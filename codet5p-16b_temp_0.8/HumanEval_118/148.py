
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

    if len(word) < 3:
        return ''
    for i in range(len(word)-1, 1, -1):
        if word[i] in 'AEIOUaeiou':
            return word[i]
        elif word[i] not in 'AEIOUaeiou' and word[i-1] not in 'AEIOUaeiou':
            continue
        else:
            return word[i]
        
    return ''

