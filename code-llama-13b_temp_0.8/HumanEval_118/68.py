
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
    vowels = ["A", "E", "I", "O", "U"]
    consonants = ["Q", "W", "R", "T", "P", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
    vowel_idx = len(word)
    for c in reversed(word):
        if c in vowels:
            vowel_idx = word.index(c)
            break
    consonant_idx = vowel_idx
    for c in reversed(word[:vowel_idx]):
        if c in consonants:
            consonant_idx = word.index(c)
            break
    return word[consonant_idx+1:vowel_idx]
