
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
    vowels = "aeiou"
    last_consonant_index = len(word)
    while last_consonant_index > 0:
        last_consonant_index -= 1
        if word[last_consonant_index] in vowels:
            break
    if last_consonant_index == 0:
        return ""
    first_consonant_index = last_consonant_index - 1
    while first_consonant_index > 0:
        if word[first_consonant_index] in vowels:
            break
        first_consonant_index -= 1
    if first_consonant_index == 0:
        return ""
    return word[first_consonant_index]

