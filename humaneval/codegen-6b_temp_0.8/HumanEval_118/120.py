
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
    
    if not word:
        return ""
    vowels = "aeiou"
    vowel_index = -1
    for i in range(len(word)-1, -1, -1):
        if word[i] in vowels:
            vowel_index = i
            break
    if vowel_index == -1:
        return ""
    
    near_vowel = word[vowel_index + 1:]
    if len(near_vowel) == 1 and near_vowel[0] in vowels:
        return word[vowel_index]
    closest_vowel = ""
    for v in vowels:
        if v in near_vowel:
            closest_vowel = v
            break
    return closest_vowel


assert(get_closest_vowel("yogurt") == "u")
assert(get_closest_vowel("FULL") == "U")
assert(get_closest_vowel("quick") == "")
assert(get_closest_vowel("ab") == "")
assert(get_closest_vowel("AA") == "")
assert(get_closest_vowel(None) == "")
assert(get_closest_vowel("") == "")

assert(get_closest_vowel("yogurt") == "u")
assert(get_closest_vowel("FULL") == "U")
assert(get_closest_vowel("quick") == "")
assert(get_closest_vowel("ab") == "")
assert(get_closest_vowel("AA") == "")
assert(get_closest_vowel(None) == "")
assert(get_closest_vowel("") == "")

