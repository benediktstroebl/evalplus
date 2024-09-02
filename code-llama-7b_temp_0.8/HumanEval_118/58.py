
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
    vowels = "aeiou"
    word = word.rstrip().lstrip()
    if len(word) == 1:
        return ""
    index = len(word) - 1
    while index > 1:
        if word[index] in vowels:
            if word[index-1] not in vowels and word[index+1] not in vowels:
                return word[index]
        index -= 1
    return ""

