
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

    start = -1
    end = len(word)
    while start+1 < end:
        mid = (start + end) // 2
        if not is_vowel(word[mid]):
            start = mid
        else:
            end = mid

    return word[end]

assert get_closest_vowel("yogurt") == "u"  
assert get_closest_vowel("FULL") == "U"
assert get_closest_vowel("quick") == ""
assert get_closest_vowel("AB") == ""
assert get_closest_vowel("kda") == "a"
assert get_closest_vowel("A") == "a"
assert get_closest_vowel("") == ""
assert get_closest_vowel("y") == "y"
