
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
    if n == 0 or word[0] == word[-1]:
        return ""
    else:
        for i in range(1, n-1):
            if word[i] == "w" or word[i] == "h" or word[i] == "y" or word[i] == "z":
                if word[i+1] == "e" or word[i+1] == "i" or word[i+1] == "o" or word[i+1] == "u":
                    if word[i] == "c" or word[i] == "g" or word[i] == "s" or word[i] == "t":
                        break
        else:
            return word[i-1]
    return ""
