
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
    n = len(word)
    for i in range(n-1):
        if word[i] == 'c' and word[i+1] == 'c':
            continue
        if word[i] == 'v' and word[i+1] == 'l':
            continue
        if word[i] == 'v' and word[i+1] == 't':
            continue
        if word[i] == 'v' and word[i+1] == 's':
            continue
        if word[i] == 'f' and word[i+1] == 'i':
            continue
        if word[i] == 'f' and word[i+1] == 'n':
            continue
        if word[i] == 'l' and word[i+1] == 'i':
            continue
        if word[i] == 'l' and word[i+1] == 'n':
            continue
        if word[i] == 'n' and word[i+1] == 'p':
            continue
        if word[i] == 'g' and word[i+1] == 'r':
            continue
        if word[i] == 'm' and word[i+1] == 'r':
            continue
        if word[i] == 'h':
            continue
        if word[i] == 'w':
            continue
        if word[i] == 'y':
            continue
        if word[i] == 'p':
            if word[i+1] in ['a', 'b', 'h', 'w']:
                return word[i+1]
        if word[i] == 'k':
            if word[i+1] == 'r':
                continue
            elif word[i+1] == 'c':
                continue
            elif word[i+1] == 'g':
                continue
            elif word[i+1] == 'm':
                continue
            elif word[i+1] == 'h':
                continue
            elif word[i+1] == 'n':
                continue
            elif word[i+1] == 'p':
                continue
            elif
