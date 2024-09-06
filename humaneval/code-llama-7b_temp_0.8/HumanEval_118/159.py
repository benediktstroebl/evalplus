
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
    
    last_vowel = -1
    vowels = []

    for i,c in enumerate(word):
        if c in 'AEIOU':
            last_vowel = i
            vowels.append(i)
    
    if last_vowel == -1:
        return ''
    elif len(vowels) == 1:
        return word[last_vowel]
    
    last_vowel_idx = len(word) - 1 - last_vowel

    for i in range(last_vowel_idx, 0, -1):
        if word[i].isupper():
            return word[i]
        if word[i].islower():
            return word[i].upper()
    
    return ''
