
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
    for i in range(len(word) - 1, -1, -1):
        if word[i] in VOWELS:
            return word[i]
    return ""


assert get_closest_vowel("yogurt") == "u"
assert get_closest_vowel("FULL") == "U"
assert get_closest_vowel("quick") == ""
assert get_closest_vowel("ab") == ""
assert get_closest_vowel("qui") == ""
assert get_closest_vowel("e") == ""
assert get_closest_vowel("") == ""


alt_ans = lambda s: ''.join(i for i in s if i.lower() in 'aeiou') or ''

alt_test = lambda s: s == ''.join(i for i in s if i.lower() in 'aeiou')


assert alt_ans('qui') == ''
assert alt_ans('e') == ''
assert alt_ans('qu') == 'qu'
assert alt_ans('quie') == 'qu'
assert alt_ans('quiuy') == 'qu'
assert alt_ans('qur') == 'qu'
assert alt_test('qui') == True
assert alt_test('e') == True
assert alt_test('qu') == True
assert alt_test('quie') == True
assert alt_test('quiuy') == True
assert alt_test('quur') == True

