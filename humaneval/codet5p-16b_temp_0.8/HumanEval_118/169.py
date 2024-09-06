
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

    vowels = "AEIOUaeiou"
    vowels_in_front = [0 for i in range(len(word))]
    vowels_in_back = [0 for i in range(len(word))]

    i = len(word) - 1
    while i >= 0:
        if word[i] in vowels:
            vowels_in_back[i] = 1
            i -= 1
        else:
            break

    i = 0
    while i < len(word):
        if word[i] in vowels:
            vowels_in_front[i] = 1
            i += 1
        else:
            break
        
    result = ""
    for i in range(len(word)):
        if vowels_in_back[i] == 1 and vowels_in_front[i] == 0 and result == "":
            result = word[i]
        elif vowels_in_back[i] == 1 and vowels_in_front[i] == 1 and result == "":
            result =
