
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
    # L|n-1 |n |n+1|n+2 |n+3 |n+4
    # A|f|e|l|l|o|r
    # 0 1 2 3 4 5 6
    # 1 2 3 4 5 6 7
    # -1  0  1  2  3  4

    vowels = ["A", "E", "I", "O", "U"]
    pos = len(word) - 1
    closest_vowel = ""

    while pos >= 2:
        if word[pos] in vowels and word[pos - 1] in vowels:
            closest_vowel = word[pos]
            break
        elif word[pos] in vowels and word[pos - 1] not in vowels:
            closest_vowel = word[pos - 1]
            break

        pos -= 1
    
    return closest_vowel

