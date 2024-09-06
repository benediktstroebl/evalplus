
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
    if len(word) == 0:
        return ""
    
    last_letter = word[-1]
    if last_letter == "y" or last_letter == "Y":
        return ""

    if last_letter in "aeiouAEIOU":
        return word[-1]
    
    index = -2
    while index >= -1:
        letter = word[index]
        if letter in "aeiouAEIOU":
            return word[index]
        index -= 1
    return ""

import unittest
