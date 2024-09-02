
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

    if len(word) == 0:
        return ""

    current_char = word[0]
    is_vowel = False
    for char in word:
        if char == current_char:
            continue
        else:
            if not is_vowel:
                current_char = char
                is_vowel = False
            elif char.upper() in vowels:
                is_vowel = True
    return current_char
