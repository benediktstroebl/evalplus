
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
    vowels = "aeiouAEIOU"
    vowel_indices = []
    for index in range(len(word)):
        if word[index] in vowels:
            vowel_indices.append(index)
    for vowel_index in vowel_indices:
        if word[vowel_index - 1].isalpha() and word[vowel_index - 1].isupper() and word[vowel_index - 1] not in vowels:
            return word[vowel_index]
        if word[vowel_index + 1].isalpha() and word[vowel_index + 1].isupper() and word[vowel_index + 1] not in vowels:
            return word[vowel_index]
    return ""

    # Alternative solution with less coding:


