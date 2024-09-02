
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
    word = word.strip()
    left_index = 0
    right_index = len(word)-1
    left_char = word[left_index]
    right_char = word[right_index]
    while not left_char.lower() in vowels:
        left_index += 1
        left_char = word[left_index]
    while not right_char.lower() in vowels:
        right_index -= 1
        right_char = word[right_index]
    if left_index >= right_index:
        return ''
    else:
        return word[left_index+1:right_index].lower()
