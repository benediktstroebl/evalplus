
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
    if len(word) < 2:
        return ""

    vowel_list = set("aeiou")
    consonant_list = set(word) - set(vowel_list)

    left_index = len(word) - 1
    right_index = 0

    while left_index >= 0 and right_index < len(word) and word[left_index] in vowel_list and word[right_index] in vowel_list:
        if word[left_index] == word[right_index]:
            left_index -= 1
        else:
            right_index += 1

    if left_index < 0:
        return ""
    return word[left_index]

