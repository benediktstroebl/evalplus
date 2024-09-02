
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
    vowel_index = 0
    for i in range(len(word) - 1):
        if word[i] == 'c' or word[i] == 's' or word[i] == 't':
            if vowel_index > 0:
                vowel_index = 0
        elif word[i] == 'h':
            vowel_index += 1
        elif word[i] == 'w' or word[i] == 'y':
            vowel_index -= 1
    if vowel_index == -1:
        return ""
    return word[vowel_index]