
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
    vowels = 'aeiou'
    right = len(word) - 1
    while right >= 0:
        right_char = word[right]
        if right_char in vowels:
            left_char = word[right - 1]
            left_right_index = right - 1
            if left_char not in vowels:
                while left_right_index > 0:
                    if left_char in vowels:
                        break
                    else:
                        left_right_index -= 1
                        left_char = word[left_right_index]
                return word[left_right_index: right + 1]
        right -= 1
    return ""
