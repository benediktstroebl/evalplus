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
    # Using find_all to find indices of all vowels and consonants
    import re
    vowels, cons = [], []
    for idx, char in enumerate(word):
        if char.lower() in 'aeiou':
            vowels.append(idx)
        elif re.search(r'[bcdfghjklmnpqrstvwxyz]', char):
            cons.append(idx)
    # If there are no consonants, return an empty string
    if not cons:
        return ""
    # If there is only 1 consonant, return the closest vowel
    if len(cons) == 1:
        return word[vowels[0] - 1]
    # If there are 2 consonants, return the closest vowel between them
    idx_diff = [abs(cons[i] - cons[i - 1]) for i in range(1, len(cons))]
    vowel_idx = vowels[idx_diff.index(min(idx_diff))]
    return word[vowel_idx - 1]