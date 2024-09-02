
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
    index = len(word) - 1
    vowels = "aeiou"
    while index >= 0:
        # check for vowel
        if word[index] in vowels:
            return word[index]
        # if index == 0:
        #     return ""
        # else:
        #     index -= 1
        index -= 1
    return ""

import unittest
