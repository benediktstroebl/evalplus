
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
    vowels = "AEIOU"
    # Converting the whole string into a list of characters
    char_list = list(word)
    
    # Iterating backwards over the list of characters
    for i in range(len(char_list) - 1, 0, -1):
        if char_list[i] in vowels and i == len(char_list) - 1:
            return word
        elif char_list[i] in vowels and char_list[i+1] in vowels:
            return word
        elif char_list[i] in vowels and char_list[i+1] not in vowels:
            return word[i]
    return ""
































