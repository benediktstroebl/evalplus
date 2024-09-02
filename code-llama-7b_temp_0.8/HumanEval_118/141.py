
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
    # get the last vowel char
    last_vowel_idx = len(word) - 1
    while last_vowel_idx >= 0:
        last_vowel_char = word[last_vowel_idx]
        if last_vowel_char.lower() in 'aeiou':
            break
        last_vowel_idx -= 1

    # no vowel
    if last_vowel_idx == -1:
        return ''

    # get the closest vowel
    first_non_vowel_idx = last_vowel_idx + 1
    while first_non_vowel_idx < len(word):
        first_non_vowel_char = word[first_non_vowel_idx]
        if first_non_vowel_char.lower() not in 'aeiou':
            break
        first_non_vowel_idx += 1
    
    if first_non_vowel_idx == len(word):
        return ''
    
    return word[last_vowel_idx]
