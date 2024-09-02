
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
    if word == '':
        return ''
    if len(word) == 1:
        return word[0]
    if word[0] in 'aeiou':
        return ''
    if word[-1] in 'aeiou':
        return word[-1]
    for letter in word:
        if letter in 'aeiou':
            return letter
    return ''

