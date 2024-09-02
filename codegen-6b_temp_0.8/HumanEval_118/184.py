
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
    syllable_count = 0
    vowel_index = 0

    for i in word[::-1]:
        if i in 'aeiou':
            vowel_index = word[::-1].index(i)
            syllable_count = len(word) - vowel_index

    return word[-syllable_count:]


assert get_closest_vowel('aeiou') == 'u'
assert get_closest_vowel('yogurt') == 'u'
assert get_closest_vowel('FULL') == 'U'
assert get_closest_vowel('quick') == ''
assert get_closest_vowel('ab') == ''
assert get_closest_vowel('abcdefghi') == ''
assert get_closest_vowel('d') == ''
assert get_closest_vowel('fghihgk') == ''
assert get_closest_vowel('fghi') == ''

