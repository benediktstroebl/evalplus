
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
    
    if len(word) == 0:
        return ''
    
    left_index = 0
    right_index = len(word) - 1
    is_vowel_found = False
    
    while left_index < right_index:
        if is_vowel(word[left_index]) and is_vowel(word[right_index]):
            left_index += 1
            right_index -= 1
        elif not is_vowel_found:
            is_vowel_found = True
            if is_vowel(word[left_index]):
                return word[left_index]
            elif is_vowel(word[right_index]):
                return word[right_index]
            left_index += 1
            right_index -= 1
        else:
            return ''
    
    return ''
