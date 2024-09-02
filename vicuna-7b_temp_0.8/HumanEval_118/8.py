
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
    word = word.upper()
    index = 1
    for i in range(len(word)-1, len(word)):
        if word[i] == "k" or word[i] == "t" or word[i] == "p" or word[i] == "s" or word[i] == "f" or word[i] == "h":
            if word[i+1] == "a" or word[i+1] == "e" or word[i+1] == "i" or word[i+1] == "o" or word[i+1] == "u":
                closest_vowel = word[index:i+2]
                return closest_vowel
            index = i
        else:
            if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
                if word[i+1] == "u" or word[i+1] == "y" or word[i+1] == "w":
                    if word[i+2] == "a" or word[i+2] == "e" or word[i+2] == "i" or word[i+2] == "o" or word[i+2] == "u":
                        return word[index:i+3]
                else:
                    index = i
    return ""