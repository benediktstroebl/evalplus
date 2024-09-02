
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
    def check_position(i):
        if vowels[i] != "a" and vowels[i] != "e" and vowels[i] != "i" and vowels[i] != "o" and vowels[i] != "u":
            return False
        elif i == 0 or vowels[i-1] == "a" or vowels[i-1] == "e" or vowels[i-1] == "i" or vowels[i-1] == "o" or vowels[i-1] == "u":
            return False
        else:
            return True
    
    vowels = word.split("")
    
    for i in range(len(vowels)-1, 0, -1):
        if check_position(i):
            return vowels[i]
    
    return ""
