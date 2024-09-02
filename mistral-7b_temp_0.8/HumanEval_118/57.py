
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


    word_list = list(word)
    left = 0
    right = len(word) - 1
    while word_list[left] in "aeiouy" or word_list[right] in "aeiouy":
        left += 1
        right -= 1
    while left < right:
        if word_list[left] in "aeiouy":
            return word_list[left]
        left += 1
    return ""
