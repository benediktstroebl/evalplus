
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
    # convert the word to upper case
    word = word.upper()
    # get the word length
    word_length = len(word)
    # iterate over the word from the end until the second last index
    for i in range(word_length-1, 0, -1):
        # get the character at the index
        character = word[i]
        # if the character is a vowel, check if it is between two consonants
        if character in "AEIOU":
            # if it is between two consonants, return the vowel
            if word[i-1].isalpha() and word[i+1].isalpha():
                return character
    # if the word doesn't contain any vowels or the vowels are at the beginning or end
    return ""
