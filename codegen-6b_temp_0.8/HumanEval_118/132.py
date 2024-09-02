
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
    if len(word) <= 1:
        return ""
    if word[-1] == word[0] is not "E":
        return word[-1]
    temp = 0
    index = len(word)-1
    while index >= 0:
        if word[index] in "AEIOU":
            if index - 1 >= 0:
                if word[index - 1] != "Y" and word[index - 1] != "W":
                    temp = index
            else:
                return word[-1]
        index -= 1
    if temp > 0:
        return word[temp-1]
    return ""

assert get_closest_vowel("yogurt") == "u"
assert get_closest_vowel("FULL") == "U"
assert get_closest_vowel("quick") == ""
assert get_closest_vowel("ab") == ""
assert get_closest_vowel("ACADEMIC") == "A"
assert get_closest_vowel("sCod") == "c"
assert get_closest_vowel("SCHOOL") == "S"
assert get_closest_vowel("MADE") == "M"
assert get_closest_vowel("FILL") == "l"
assert get_closest_vowel("flab") == "f"
assert get_closest_vowel("WALL") == "A"
assert get_closest_vowel("LEARNED") == "N"