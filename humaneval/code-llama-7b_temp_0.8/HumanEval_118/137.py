
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
    vowels = "aeiouAEIOU"
    first_vowel_pos = -1
    last_vowel_pos = -1
    word = word.lower()

    for index, letter in enumerate(word):
        if letter in vowels and first_vowel_pos == -1:
            first_vowel_pos = index
        elif letter in vowels:
            last_vowel_pos = index

    if first_vowel_pos == -1 or last_vowel_pos == -1:
        return ""
    if last_vowel_pos - first_vowel_pos == 1:
        return word[first_vowel_pos]
    if last_vowel_pos - first_vowel_pos == 2:
        return word[first_vowel_pos + 1]
    return ""

