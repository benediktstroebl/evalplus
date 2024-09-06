
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
    vowels = 'aeiou'
    left_side = [char for char in word if char in vowels]
    left_side = left_side[::-1]
    right_side = [char for char in word if char in vowels]
    index = word.index(right_side[0])
    left_index = word.rindex(left_side[0])
    if len(left_side) > 1:
        left_index = word.rindex(left_side[1])
    if index - left_index > 1:
        return word[left_index + 1]
    return ''
    
