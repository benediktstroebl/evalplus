
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
    return_str = ""
    last_index = len(word)-1
    last_char = word[last_index]
    if last_char == "a" or last_char == "e" or last_char == "i" or last_char == "o" or last_char == "u":
        return word
    else:
        for i in range(last_index,0,-1):
            if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
                return_str = word[i+1:last_index+1]
                return return_str
    return return_str
