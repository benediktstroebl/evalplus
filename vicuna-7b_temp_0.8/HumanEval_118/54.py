
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
    i = len(word) - 1
    while i >= 0 and word[i] == 'c':
        i -= 1
    if i < 0:
        return ""
    while i >= 0 and word[i] == 's':
        i -= 1
    if i < 0:
        return ""
    start = i
    while i >= 0 and word[i] == 't':
        i -= 1
    if i < 0:
        return ""
    while i >= 0 and word[i] == 'p':
        i -= 1
    if i < 0:
        return ""
    stop = i
    while i >= 0 and word[i] == 'l':
        i -= 1
    if i < 0:
        return ""
    start = min(start, stop)
    vowels = set(string.ascii_letters)[:2]
    return word[start:stop] if start < stop else ""