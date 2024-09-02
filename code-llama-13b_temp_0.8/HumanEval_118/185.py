
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
    # make a list of all vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    # loop through the letters in the word backwards
    for i in range(len(word) - 1, 0, -1):
        # if the current letter is a vowel, and the next letter is a consonant, return the vowel
        if word[i] in vowels and word[i - 1] not in vowels:
            return word[i]
    # if no vowel was found, return an empty string
    return ""

