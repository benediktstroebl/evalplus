
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

    vowels = ["a","e","i","o","u"]
    word = word.lower()
    for i in range(len(word)-1):
        if (word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u" or word[i] == "y") and (word[i+1] == "a" or word[i+1] == "e" or word[i+1] == "i" or word[i+1] == "o" or word[i+1] == "u" or word[i+1] == "y"):
            if (word[i+1] == "a" or word[i+1] == "e" or word[i+1] == "i" or word[i+1] == "o" or word[i+1] == "u" or word[i+1] == "y"):
                return word[i+2]
            else:
                return word[i+1]
