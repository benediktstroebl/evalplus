
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
    vowels = {'a', 'e', 'i', 'o', 'u'}

    left_index = 0
    right_index = len(word) - 1

    while left_index < right_index:
        left_char = word[left_index]
        right_char = word[right_index]
        if left_char not in vowels and right_char not in vowels:
            return ""
        else:
            left_index += 1
            right_index -= 1

    return word[left_index] if left_index < right_index else
