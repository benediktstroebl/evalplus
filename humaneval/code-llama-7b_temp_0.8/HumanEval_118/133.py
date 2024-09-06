
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
    last_index = len(word) - 1
    word_upper = word.upper()
    vowels = ['A', 'O', 'E', 'I', 'U']
    for index in range(len(word_upper)):
        if word_upper[index] not in vowels:
            continue
        right_index = index + 1
        left_index = index - 1
        while word_upper[right_index] not in vowels:
            if right_index == last_index:
                return ''
            right_index += 1
        while word_upper[left_index] not in vowels:
            if left_index == 0:
                return ''
            left_index -= 1
        return word[left_index]
    return ''
