
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
    vowel = ''
    vowel_pos = []
    for i, letter in enumerate(word[::-1]):
        if letter in 'AEIOU':
            vowel_pos.append(len(word) - i)
    if vowel_pos:
        vowel = word[vowel_pos[-1] - 1]
    return vowel

