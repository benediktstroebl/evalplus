
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
    vowels = 'aeiouAEIOU'
    char_list = list(word)
    for i, char in enumerate(char_list):
        if char not in vowels:
            continue
        if i == 0 or i == len(char_list) - 1:
            continue
        if char_list[i - 1] not in vowels and char_list[i + 1] not in vowels:
            return char
    return ''

