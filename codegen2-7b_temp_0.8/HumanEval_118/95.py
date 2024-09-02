
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
    word = word.strip()
    if not word or len(word) == 0:
        return ""

    vowels = ["a","e","i","o","u"]
    if word[0] not in vowels:
        return ""

    vowel_index = -1
    for i in range(len(word)):
        if word[i] not in vowels:
            vowel_index = i
            break

    if vowel_index == -1:
        return ""

    return word[vowel_index-1]
