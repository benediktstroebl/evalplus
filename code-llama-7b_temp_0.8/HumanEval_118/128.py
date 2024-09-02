
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
    # Rules:
    # 1. It must be a vowel between two consonants
    # 2. It must be the closest vowel
    # 3. It must be from the right side
    # 4. It can be in the middle of the word
    # 5. It must be case sensitive

    # vowels = ["A", "E", "I", "O", "U"] # can't use this
    vowels = ["a", "e", "i", "o", "u"] # can't use this
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    
    # Approach:
    # Loop from the right side of the word. If the character is a vowel, check if it's the closest to two consonants
    # If it's the closest, return the vowel.

    # word = "yogurt"
    # word = "FULL"
    # word = "quick"
    # word = "ab"
    # word = "AQQQ"

    # 1st solution
    # loop through the word from the right side
    # if character is a vowel, return
    # if character is a consonant, move to the next
    # once you reach the end of the word, return ""

    # for character in reversed(word):
    #     if character in vowels:
    #         return character
    #     elif character in consonants:
    #         pass
    # return ""

    # 2nd solution
    # run loop from the right side
    # use two variables to track the closest vowel and consonant to the right
    # if character is a vowel, check if it's the closest to two consonants
    # if so, return it.
    # if character is a consonant, update the closest vowel and consonant

    # initialize the variables
    closest_vowel = ""
