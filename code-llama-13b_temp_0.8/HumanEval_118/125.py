
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
    word = word.lower()
    vowels = 'aeiou'
    vowel_idx = [i for i, x in enumerate(word) if x in vowels and i != 0 and i != len(word)-1]
    consonant_idx = [i for i, x in enumerate(word) if x not in vowels and i != 0 and i != len(word)-1]
    
    if len(vowel_idx) == 0 or len(consonant_idx) == 0:
        return ''
    
    for i in range(len(consonant_idx)-1, -1, -1):
        if consonant_idx[i] < vowel_idx[0]:
            return ''
        for j in range(len(vowel_idx)-1, -1, -1):
            if consonant_idx[i] > vowel_idx[j]:
                return word[vowel_idx[j]]
    
    return word[vowel_idx[0]]
