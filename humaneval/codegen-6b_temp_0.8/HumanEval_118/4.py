
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
    left = ""
    right = word[-1]
    left_max_index = len(word) - 1 - word[::-1].find(right)
    for c in word[:left_max_index]:
        left += c
    right_max_index = word.find(right)
    for c in word[right_max_index:]:
        right += c
    vowels = string.ascii_lowercase
    return left + get_closest_vowel(right)
