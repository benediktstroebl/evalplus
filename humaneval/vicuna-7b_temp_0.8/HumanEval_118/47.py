
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
    right_half = word[::2]
    left_half = word[1::2]
    left_index = len(left_half) - 1
    for i in range(len(right_half)):
        if right_half[i] == left_half[i] and right_half[i + 1] == left_half[i + 1]:
            left_index -= 1
            if left_index < 0:
                return " "
        elif right_half[i] == left_half[i] and right_half[i + 1] != left_half[i + 1]:
            return left_half[i]
    return ""
