
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
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    vowel_indexes = []

    for i in range(len(word)):
        if word[i] in vowels:
            vowel_indexes.append(i)
        
    
    for j in range(len(vowel_indexes)-1):
        if vowel_indexes[j+1] - vowel_indexes[j] == 1:
            return word[vowel_indexes[j]]
    
    return ""

assert get_closest_vowel("yogurt") == "u"
assert get_closest_vowel("FULL") == "U"
assert get_closest_vowel("quick") == ""
assert get_closest_vowel("ab") == ""
assert get_closest_vowel("yee") == ""
assert get_closest_vowel("zoo") == ""
assert get_closest_vowel("zy") == ""
assert get_closest_vowel("ab") == ""
assert get_closest_vowel("A") == ""
