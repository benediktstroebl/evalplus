
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

    word = word.lower()
    vowels = "aeiouAEIOU"

    # convert the word to lowercase
    word = word.lower()

    # check if the word is empty
    if not word:
        return ""

    # split the word into a list of characters
    word_list = word.split()

    # initialize position of vowel
    vowel_pos = 0

    # check if the word contains only one vowel
    if len(word_list) == 1:
        vowel_pos = 0
    else:
        # find the index of the first consonant
        first_consonant_idx = word_list.index(word_list[0])
        # find the index of the second consonant
        second_consonant_idx = word_list.index(word_list[-1], first_consonant_idx)

        # check if the second consonant is the last character of the word
        if second_consonant_idx == len(word_list) - 1:
            vowel_pos = len(word_list)
        else:
            vowel_pos = second_consonant_idx + 1

    # find the index of the closest vowel
    closest_vowel_idx = vowel_pos - 1

    # check if the closest vowel is the first vowel
    if closest_vowel_idx == 0:
        return ""

    # return the closest vowel
    return word_list[closest_vowel_idx]
