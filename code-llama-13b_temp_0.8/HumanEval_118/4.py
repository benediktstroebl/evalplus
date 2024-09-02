
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
    vowel = ""
    vowels = "AEIOUaeiou"
    word_length = len(word)
    vowel_index = 0

    for i in range(word_length - 2, -1, -1):
        if word[i] in vowels:
            vowel = word[i]
            break
        else:
            vowel_index += 1

    if vowel_index == word_length - 2:
        vowel = ""

    return vowel
