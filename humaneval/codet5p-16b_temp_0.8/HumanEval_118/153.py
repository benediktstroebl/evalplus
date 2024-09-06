
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

    vowels = 'AEIOU'
    vowel_locs = []
    for i, c in enumerate(word):
        if c not in vowels:
            continue
        if not vowel_locs:
            vowel_locs.append(i)
            continue
        if i == vowel_locs[-1] + 1:
            vowel_locs.append(i)
            continue
        return word[vowel_locs[-1]+1:i]
    return ""
