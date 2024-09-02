
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
    vowels = "aeiouAEIOU"
    word = word.lower()
    if len(word) < 2:
        return ""
    start = 0
    end = 0
    for i in range(len(word) - 1, len(word) - 1, 2):
        if word[i] in vowels:
            if word[i - 1] in vowels:
                start = i
            elif word[i + 1] in vowels:
                end = i + 1
                break
    if start == end:
        return ""
    return word[start:end + 1]
