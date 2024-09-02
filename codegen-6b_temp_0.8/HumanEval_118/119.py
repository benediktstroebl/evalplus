
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
    index_of_last_vowel = len(word) - 1
    vowel_to_move = ""
    while len(vowel_to_move) == 0:
        if index_of_last_vowel == 0:
            return word[0]
        if word[index_of_last_vowel] in vowels:
            vowel_to_move = word[index_of_last_vowel]
        index_of_last_vowel -= 1
    move_direction = 1 if vowel_to_move == vowels[0] else -1
    for x in range(index_of_last_vowel, len(word)):
        if word[x] in vowels:
            return word[x]
    return word[0]
