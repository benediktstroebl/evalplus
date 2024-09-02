
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
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    char_list = list(word)
    if len(char_list) == 0:
        return ""
    vowel_index = []
    for i in range(len(word)):
        if word[i] in vowels:
            vowel_index.append(i)
    if len(vowel_index) == 0:
        return ""
    vowel_index.sort()
    for i in vowel_index:
        if i == len(word) - 1:
            return ""
        for j in range(i + 1, len(word)):
            if word[j] in consonants and word[j - 1] in consonants:
                return word[j]
    return ""

