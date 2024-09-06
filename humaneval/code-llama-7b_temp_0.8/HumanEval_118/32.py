
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
    vowels = "AEIOUaeiou"
    vowels_index = []
    for i in range(len(word)):
        if word[i] in vowels:
            vowels_index.append(i)

    if len(vowels_index) < 2:
        return ""
    elif len(vowels_index) == 2:
        if vowels_index[1] - vowels_index[0] == 1:
            return word[vowels_index[1]]
        return ""

    for i in range(len(vowels_index) - 2, 0, -1):
        if vowels_index[i] - vowels_index[i - 1] > 1:
            return word[vowels_index[i]]
    return ""

