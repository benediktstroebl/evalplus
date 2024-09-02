
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
    # initialize variables with default values
    left_most_vowel = ''
    previous_letter = ''
    current_index = 0

    # loop through each character of the word
    for i in range(len(word)):
        # if the current character is a vowel and previous character is a consonant
        if word[i] in ['a', 'e', 'i', 'o', 'u'] and previous_letter in ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'z']:
            # find the index of the closest vowel
            current_index = i
            left_most_vowel = previous_letter
        # if the current character is a consonant
        elif word[i] in ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'z']:
            # if the previous character is a vowel
            if previous_letter in ['a', 'e', 'i', 'o', 'u']:
                # set the previous character to the closest vowel
                previous_letter = left_most_vowel
            # set the current character as previous character
            previous_letter = word[i]
        # update the current index
        current_index += 1

    return left_most_vowel
