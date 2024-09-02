
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
    vowels = u'aeiou'
    vowel_positions = [n for n,i in enumerate(word) if i in vowels]

    if not vowel_positions:
        return ''

    left = max(0, min(vowel_positions) - 1)
    right = max(vowel_positions) + 1
    for i in range(left, right):
        vowels_shifted = vowels[vowels.find(word[i]):]
        if vowels_shifted:
            return vowels_shifted[0]

    return ''

assert get_closest_vowel("yogurt") == "u"
assert get_closest_vowel("FULL") == "U"
assert get_closest_vowel("quick") == ""
assert get_closest_vowel("ab") == ""
assert get_closest_vowel("aab") == "a"
assert get_closest_vowel("zoologi") == "o"
assert get_closest_vowel("abcd") == ""
assert get_closest_vowel("codsoo") == ""
assert get_closest_vowel("a") == ""
assert get_closest_vowel("A") == ""
assert get_closest_vowel("Frc") == ""
assert get_closest_vowel("FrcAke") == "a"
assert get_closest_vowel("b") == ""
assert get_closest_vowel("classey") == ""
assert get_closest_vowel("Acla") == "a"
assert get_closest_vowel("s") == ""
assert get_closest_vowel("awww") == ""
assert get_closest_vowel("awwwj") == ""
assert get_closest_vowel("awe") == ""
assert get_closest_vowel("a") == ""
