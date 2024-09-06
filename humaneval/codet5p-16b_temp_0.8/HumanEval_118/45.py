
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

    
    word_list = list(word)
    vowels = ["A", "E", "I", "O", "U"]
    
    for i in range(len(word_list)-1, -1, -1):
        if word_list[i].isalpha():
            if word_list[i+1].isalpha():
                if word_list[i].upper() not in vowels:
                    return word_list[i]
            elif word_list[i-1].isalpha():
                if word_list[i].upper() not in vowels:
                    return word_list[i]
            else:
                return ""
    
    return ""
    
    
