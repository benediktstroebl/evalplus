
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

    vowels = "aeiouAEIOU"
    vowel_idx = []
    consonant_idx = []
    for idx, char in enumerate(word):
        if char in vowels:
            vowel_idx.append(idx)
        else:
            consonant_idx.append(idx)
    
    if len(consonant_idx) == 0 or len(consonant_idx) == len(word):
        return ""

    for i in range(len(vowel_idx)):
        idx = vowel_idx[i]
        if idx - 1 in consonant_idx and idx + 1 in consonant_idx:
            return word[idx]

    return ""
