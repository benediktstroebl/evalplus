
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

    from itertools import zip_longest
    from string import ascii_lowercase

    vowels = list(ascii_lowercase[:5] + ascii_lowercase[-5:])
    vowels = [vowel for vowel in vowels if vowel.lower() not in word.lower()]

    def get_closest(word):
        vowel_pairs = zip_longest(word, word[1:], fillvalue='')
        for vowel, next_letter in vowel_pairs:
            if vowel in vowels and next_letter in vowels:
                return vowel
        return ''

    return get_closest(word)

