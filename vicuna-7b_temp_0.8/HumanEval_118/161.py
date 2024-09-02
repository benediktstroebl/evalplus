
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
    if len(word) == 1:
        return ""
    last_char = word[-1]
    for i in range(len(word)-1, 0, -1):
        prev_char = word[i]
        if prev_char == last_char and prev_char == word[i+1] and (word[i+2] in "aeiou" or word[i+2] == "y"):
            return word[i]
    return ""