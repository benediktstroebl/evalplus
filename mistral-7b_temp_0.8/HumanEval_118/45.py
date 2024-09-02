
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

    vowels = ["a", "e", "i", "o", "u"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    vowels.extend(consonants)
    word_list = list(word)
    vowel_index = 0
    consonant_index = 0
    for i in range(len(word_list)):
        if word_list[i] in vowels:
            vowel_index = i
        if word_list[i] in consonants:
            consonant_index = i
            break
    if vowel_index >= consonant_index:
        return ""
    else:
        return word_list[vowel_index]
    """
    *Bonus:
    - if you can finish in less than 10 lines of code,
