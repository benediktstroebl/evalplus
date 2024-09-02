
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
    word = word.lower()
    half_word = len(word) // 2
    start = half_word
    end = len(word) - half_word
    vowel_chars = "aeiou"
    if start == 0:
        start += 1
    while start < end:
        index = len(word) - start
        if word[index] in vowel_chars:
            return word[start:index+1]
        start += 1
    return ""
