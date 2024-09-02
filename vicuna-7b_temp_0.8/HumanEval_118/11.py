
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
    # remove all non-alphanumeric characters from the word
    word = "".join(filter(str.isalnum, word))

    # split the word into a list of subwords
    subwords = word.split()

    # get a list of all vowels
    vowels = "aeiouAEIOU"

    # iterate through each subword and check if it contains a vowel
    for i, subword in enumerate(subwords):
        if subword in vowels:
            return subword
        elif i > 0 and subwords[i-1] == subwords[i]:
            # check if the previous subword is a consonant
            if not subwords[i-1].isalpha():
                return subword

    # if none of the subwords contains a vowel, return an empty string
    return ""