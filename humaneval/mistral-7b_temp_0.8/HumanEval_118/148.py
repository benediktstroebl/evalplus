
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

    """
    Use the built-in function `isalpha()` to test whether a string is a letter or not.
    You may assume that only the English letters exist.
    """

    word = word.lower()
    vowels = ['a','e','i','o','u']

    if word.isalpha():
        if 'a' in word:
            first_a = word.index('a')
            first_a = word[first_a + 1]
        else:
            first_a = ''
        if 'e' in word:
            first_e = word.index('e')
            first_e = word[first_e + 1]
        else:
            first_e = ''
        if 'i' in word:
            first_i = word.index('i')
            first_i = word[first_i + 1]
        else:
            first_i = ''
        if 'o' in word:
            first_o = word.index('o')
            first_o = word[first_o + 1]
       
