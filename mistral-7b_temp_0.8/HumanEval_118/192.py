
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
    if len(word) < 4:
        return ''

    letters = ['a', 'e', 'i', 'o', 'u']

    first_vowel = word[0]
    last_vowel = word[-1]

    left_letters = list(word[:word.find(first_vowel)])
    right_letters = list(word[word.find(last_vowel) + 1:])

    if all(letter in letters for letter in left_letters) and all(letter in letters for letter in right_letters):
        return ''

    for letter in left_letters:
        if letter in letters:
            return letter
    for letter in right_letters:
        if letter in letters:
            return letter
    return ''

































































