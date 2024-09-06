
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
    if len(word) < 2:
        return ""
    for i in range(len(word)-1):
        for j in range(i+1, len(word)):
            if word[i] == word[j] and word[i+1] == word[j+1]:
                if word[i] == "b" or word[i] == "d" or word[i] == "f" or word[i] == "h" or word[i] == "j" or word[i] == "k" or word[i] == "l" or word[i] == "m" or word[i] == "n" or word[i] == "p" or word[i] == "r" or word[i] == "s" or word[i] == "t" or word[i] == "v" or word[i] == "w" or word[i] == "x" or word[i] == "y" or word[i] == "z":
                    continue
                elif word[i] == "a" and word[j] == "e" or word[i] == "e" and word[j] == "i" or word[i] == "i" and word[j] == "u" or word[i] == "o" and word[j] == "u" or word[i] == "u" and word[j] == "a":
                    if word[i+1] == "a" and word[j+1] == "e" or word[i+1] == "e" and word[j+1] == "i" or word[i+1] == "i" and word[j+1] == "u" or word[i+1] == "o" and word[j+1] == "u" or word[i+1] == "u" and word[j+1] == "a":
                        return word[i]
    return ""
