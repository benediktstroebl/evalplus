
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
    result = []
    vowels = ["a", "e", "i", "o", "u"]
    left_index = 0
    right_index = len(word) - 1

    while left_index <= right_index:
        if word[left_index] in vowels:
            left_index += 1
            continue
        if word[right_index] in vowels:
            right_index -= 1
            continue
        if abs(left_index - right_index) > 1:
            break
        if abs(left_index - right_index) == 1:
            result.append(word[left_index])
        left_index += 1
        right_index -= 1
    return "".join(result)

