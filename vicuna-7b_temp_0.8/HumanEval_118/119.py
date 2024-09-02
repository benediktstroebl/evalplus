
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
    word = "".join(word)
    vowel_index = -1
    for i in range(len(word)-1, 0, -1):
        if (word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u") and word[i+1] in ["b", "c", "d", "f", "g", "h", "j", "k", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]:
            vowel_index = i
            break
    return vowel_index
