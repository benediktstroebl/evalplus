
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
    first_closest_vowel, second_closest_vowel = get_consonants_and_vowels(word)
    if first_closest_vowel == second_closest_vowel:
        return ''
    elif second_closest_vowel > first_closest_vowel:
        return second_closest_vowel
    else:
        return first_closest_vowel
