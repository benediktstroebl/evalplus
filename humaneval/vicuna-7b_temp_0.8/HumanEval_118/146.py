
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
    # Use list comprehension to create a list of all vowels in the word
    vowels = [c for c in word if c.isupper() and c.isalpha() and c.isvowel()]

    if not vowels:
        return ""

    first_vowel = min(vowels, key=vowels.index)
    second_vowel = max(vowels, key=vowels.index)

    return first_vowel
