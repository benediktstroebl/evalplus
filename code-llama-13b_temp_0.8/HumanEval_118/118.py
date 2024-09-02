
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_upper = [v.upper() for v in vowels]
    letters = list(word)
    letters_upper = [l.upper() for l in letters]
    vowels_in_word = [letter for letter in letters if letter in vowels or letter in vowels_upper]
    if len(vowels_in_word) < 2:
        return ''

    vowels_in_word_right = vowels_in_word[::-1]
    for i in range(len(vowels_in_word_right)-1):
        if (vowels_in_word_right[i] in vowels and vowels_in_word_right[i+1] in vowels) or \
           (vowels_in_word_right[i] in vowels_upper and vowels_in_word_right[i+1] in vowels_upper):
            return vowels_in_word_right[i]
    return ''
