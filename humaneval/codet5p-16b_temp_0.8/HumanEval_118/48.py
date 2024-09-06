
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
    vowel_counter = 0
    vowel_index = 0
    i = len(word)-1
    while i >= 0:
        if word[i] in vowels:
            if vowel_counter == 0:
                vowel_index = i
            vowel_counter += 1
        i -= 1

    if vowel_counter > 1:
        vowel_index = vowel_index + 1
    if vowel_index == 0:
        return ""
    else:
        return word[vowel_index]

