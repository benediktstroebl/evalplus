
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
    # create a list of all vowels
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    # create a list of all consonants
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
    # create a list of the word's letters
    letters = [i for i in word]
    # reverse the letters list
    letters.reverse()
    # create a boolean
    is_vowel = False
    # loop through the reversed letters
    for letter in letters:
        # if the letter is a vowel
        if letter in vowels:
            # set is_vowel to True
            is_vowel = True
            # continue to the next letter
            continue
        # if the letter is a consonant and is_vowel is True
        if letter in consonants and is_vowel:
            # return the letter
            return letter
    # if is_vowel is False
    if not is_vowel:
        # return an empty string
        return ""
