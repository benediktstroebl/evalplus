
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
    vowel_list = ["a","e","i","o","u"]
    closest = ""
    word_list = list(word)
    for i in range(len(word_list)):
        if word_list[i].lower() in vowel_list:
            if i>1 and word_list[i-1].lower() not in vowel_list:
                if i<len(word_list)-1 and word_list[i+1].lower() not in vowel_list:
                    closest = word_list[i].lower()
    return closest
