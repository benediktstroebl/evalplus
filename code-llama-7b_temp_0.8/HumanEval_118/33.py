
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

    word = word.upper()
    vowels_in_word = [char for char in word if char in vowels]

    if len(vowels_in_word) < 2:
        return ""

    for i in range(len(vowels_in_word)-2, 0, -1):
        if vowels_in_word[i-1] in vowels and vowels_in_word[i+1] in vowels:
            return vowels_in_word[i]
    
    return ""

