
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
    left_index = len(word) - 1
    right_index = 0

    while right_index < len(word) and word[right_index] == 'c':
        right_index += 1
    while right_index < len(word) and word[right_index] == 's':
        right_index += 1
    while right_index < len(word) and word[right_index] == 't':
        right_index += 1

    if right_index == len(word) or word[right_index] not in ['a', 'e', 'i', 'o', 'u']:
        return ''

    close_index = right_index - 1
    while word[close_index] == 'c' or word[close_index] == 's' or word[close_index] == 't':
        close_index -= 1
    while word[close_index] == 'r' or word[close_index] == 's' or word[close_index] == 't':
        close_index += 1

    return word[close_index]