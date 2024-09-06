
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
    # your code goes here
    word = word.lower()
    vowels = 'aeiou'
    if len(word) <= 2:
        return ''

    closest_index = float('inf')
    closest_vowel = ''
    for index, char in enumerate(word):
        if char in vowels:
            if (index - 1) > closest_index:
                closest_index = index
                closest_vowel = char
            if index - 1 < closest_index:
                closest_index = index
                closest_vowel = char
    return closest_vowel


