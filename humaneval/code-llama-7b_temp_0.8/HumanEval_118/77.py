
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
    vowels = "aeiou"
    vowel_index = []
    # find vowels
    for i, v in enumerate(word):
        if v in vowels:
            vowel_index.append(i)

    # check if there is vowel in between consonants
    for i in range(len(vowel_index) - 1, 0, -1):
        if vowel_index[i] - vowel_index[i - 1] > 1:
            return word[vowel_index[i-1]]

    return ""

