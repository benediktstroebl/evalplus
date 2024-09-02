
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
    # convert word to lowercase
    word = word.lower()
    # split the word to list of characters
    word_chars = word.split()
    # check all the characters in word_chars
    for char in word_chars:
        # check if the char is a vowel
        if char in "aeiou":
            # check if char is the closest vowel between the rightmost consonant
            # and the rightmost position
            if char.upper() in word_chars[:word_chars.index(char)+1] and word_chars[word_chars.index(char)+1].upper() == char.upper():
                return char.upper()
    return ""