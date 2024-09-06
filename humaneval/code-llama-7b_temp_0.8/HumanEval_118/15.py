
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
    # RW + ITER + STRING FUNCTIONS
    vowels = 'aeiouy'
    last_consonant_idx = len(word) - 1
    
    # Since vowels are in the end of the string,
    # there's no need to go backwards
    while word[last_consonant_idx] not in vowels:
        last_consonant_idx -= 1
        
        # We went too far
        if last_consonant_idx < 0:
            return ""
        
    for idx in range(last_consonant_idx, -1, -1):
        if word[idx] in vowels:
            return word[idx]

    return ""
