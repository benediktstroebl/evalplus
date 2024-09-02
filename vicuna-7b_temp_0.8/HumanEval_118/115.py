
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
    if len(word) < 2:
        return ""
    for i in range(len(word) - 2, -1, -1):
        for j in range(i + 1, len(word)):
            if word[i] == word[j] and word[i+1] == word[j+1]:
                continue
            if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
                if word[j] == "a" or word[j] == "e" or word[j] == "i" or word[j] == "o" or word[j] == "u":
                    continue
                break
    return ""