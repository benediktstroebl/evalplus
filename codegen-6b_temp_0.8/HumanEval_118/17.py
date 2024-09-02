
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
    vowels = {'a':'A', 'e':'E', 'i':'I', 'o':'O', 'u':'U'}
    v = []
    for index in range(len(word) - 1, -1, -1):
        if word[index] in vowels:
            v.append(vowels[word[index]])
        elif word[index].isalpha() and word[index].isupper():
            v.append('A')
        else:
            v.append('')
    return v[::-1][0]

assert get_closest_vowel("YUGRT") == "U"
assert get_closest_vowel("FULL") == "U"
assert get_closest_vowel("quick") == ""
assert get_closest_vowel("ab") == ""
assert get_closest_vowel("") == ""
assert get_closest_vowel("a") == ""

