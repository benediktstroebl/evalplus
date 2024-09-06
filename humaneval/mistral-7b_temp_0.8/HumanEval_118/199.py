
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
    first_consonant_idx = None
    second_consonant_idx = None
    vowels = "aeiou"
    for idx, char in enumerate(word):
        if not char in vowels:
            if first_consonant_idx is None:
                first_consonant_idx = idx
            elif second_consonant_idx is None:
                second_consonant_idx = idx
        elif first_consonant_idx is not None and second_consonant_idx is not None:
            break
    if first_consonant_idx is not None and second_consonant_idx is not None:
        for i in range(first_consonant_idx+1, second_consonant_idx):
            if word[i] in vowels:
                return word[i]
    return ""

