
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

    vowels = ["a", "e", "i", "o", "u"]
    max_len = -1
    res = ""
    for i in range(len(word)):
        if word[i] in vowels:
            start_vowel = i
            for j in range(len(word) - 1, i, -1):
                if word[j] not in vowels:
                    if j - i > max_len:
                        max_len = j - i
                        res = word[j]
                    break
    return res
