
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
    # reverse the word
    word = word[::-1]
    
    # check for vowel in the right side
    i = len(word) - 1
    for j in range(len(word)-1, -1, -1):
        if word[j] == word[i] and word[j+1] == word[i+1] and word[j] == "a" or word[j] == "e" or word[j] == "i" or word[j] == "o" or word[j] == "u" or word[j] == "A" or word[j] == "E" or word[j] == "I" or word[j] == "O" or word[j] == "U":
            return word[j]
    return ""
