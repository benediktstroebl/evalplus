
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
    # Determine the last consonant
    index_consonant = len(word) - 1
    while index_consonant >= 0 and word[index_consonant].lower() in "aeiou":
        index_consonant -= 1
    # If no consonant is found, return empty string
    if index_consonant < 0:
        return ""
    # Determine the second last consonant
    index_consonant2 = index_consonant - 1
    while index_consonant2 >= 0 and word[index_consonant2].lower() in "aeiou":
        index_consonant2 -= 1
    # If second last consonant is the same as the last consonant, return empty string
    if index_consonant2 == index_consonant:
        return ""
    # Otherwise, return the vowel from the second last consonant
    return word[index_consonant2]

