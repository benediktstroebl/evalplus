
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

    closest_vowel = ""
    for i in range(len(word)):
        if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
            if i < len(word) - 1 and (word[i]!= "a" and word[i]!= "e" and word[i]!= "i" and word[i]!= "o" and word[i]!= "u" and word[i+1]!= "a" and word[i+1]!= "e" and word[i+1]!= "i" and word[i+1]!= "o" and word[i+1]!= "u"):
                return word[i]
            elif i == len(word) - 1:
                return word[i]
    return closest_vowel


