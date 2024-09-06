
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

    # your code here
    # return ""
    #last consonant, prev_consonant, vowel
    vowels = 'aeiou'
    # go through word and check for consonants
    consonant = False
    for letter in word:
        if letter in vowels:
            continue
        if letter not in vowels:
            consonant = True
            if consonant and prev_consonant:
                return letter
        prev_consonant = consonant

    return ""

