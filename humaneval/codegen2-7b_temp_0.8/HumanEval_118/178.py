
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
    vowels = ("a", "e", "i", "o", "u", "y")
    vowel_position = 0
    word_length = len(word)
    for i in range(word_length):
        for j in vowels:
            if word[i] == j:
                vowel_position = i
    if vowel_position == 0 or vowel_position == word_length - 1:
        return ""
    return word[vowel_position - 1]

