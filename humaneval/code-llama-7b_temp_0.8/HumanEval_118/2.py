
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
    # [::-1] reverses the order of the string
    # index() gets the index of the element in the list
    # f-string formatting: format(f'{variable}')
    # .replace('_', '') removes the underscores
    return word[word[::-1].index(max(filter(lambda x: x in 'AEIOU', word[1:-1]), default='_'))]
