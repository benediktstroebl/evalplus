
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
    current_index = len(word) - 1
    previous_index = len(word) - 2
    closest_vowel = ''
    while current_index >= 0 and previous_index >= 0:
        if word[current_index] == 'c' and word[previous_index] in 'sdfghjkkllmnprstvwxz' and \
           word[current_index-1] == 'r':
            closest_vowel = 'r'
        elif word[current_index] == 'b' and word[previous_index] in 'sdfghjkkllmnprstvwxz' and \
           word[current_index-1] == 'n':
            closest_vowel = 'n'
        elif word[current_index] == 'l' and word[previous_index] in 'sdfghjkkllmnprstvwxz' and \
           word[current_index-1] == 't':
            closest_vowel = 't'
        elif word[current_index] == 'p' and word[previous_index] in 'sdfghjkkllmnprstvwxz' and \
           word[current_index-1] == 'i':
            closest_vowel = 'i'
        elif word[current_index] == 'd' and word[previous_index] in 'sdfghjkkllmnprstvwxz' and \
           word[current_index-1] == 'g':
            closest_vowel = 'g'
        current_index -= 1
        previous_index -= 1
    return closest_vowel