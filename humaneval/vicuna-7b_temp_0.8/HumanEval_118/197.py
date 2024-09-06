
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
    start = 0
    for i in range(len(word)):
        if word[i] == "r" and word[i-1] == "c":
            start = i+1
        elif word[i] == "l" and word[i-1] == "s":
            start = i+1
        elif word[i] == "n" and word[i-1] == "d":
            start = i+1
        elif word[i] == "t" and word[i-1] == "p":
            start = i+1
        elif word[i] == "f" and word[i-1] == "b":
            start = i+1
        elif word[i] == "v" and word[i-1] == "b":
            start = i+1
            
        if start != len(word):
            if word[start] == "a" or word[start] == "e" or word[start] == "i" or word[start] == "o" or word[start] == "u":
                return word[start]
    return ""
