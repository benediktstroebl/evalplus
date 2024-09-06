
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
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for i in range(len(word)):
        if word[i] == 'a':
            a = 1
        if word[i] == 'e':
            e = 1
        if word[i] == 'i':
            i = 1
        if word[i] == 'o':
            o = 1
        if word[i] == 'u':
            u = 1

    word = word.lower()
    if a == 0 and e == 0 and i == 0 and o == 0 and u == 0:
        return ""

    for i in range(len(word)-1):
        if word[i] == "s" and word[i+1] == "n" and word[i+2] == "s" and word[i+3] == "b" and word[i+4] == "t" and word[i+5] == "m":
            return ""
        if word[i
