
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
    idx = len(word)
    for i, letter in enumerate(word):
        if letter in VOWELS:
            idx = i
            break
    
    if idx == len(word):
        return ""

    
    ch = word[idx]
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        return ""
    
    # 1. Get the index of previous consonant
    prev = idx - 1
    while True:
        if word[prev] not in VOWELS:
            prev -= 1
            continue
        else:
            break
    
    # 2. Get the index of next consonant
    next = idx + 1
    while True:
        if word[next] not in VOWELS:
            next += 1
            continue
        else:
            break
    
    while next < len(word) and word[next] not in VOWELS:
        next += 1
    
    next -= 1
    
    return word[prev:idx] + word[next] + word[idx+1:next]
    
    