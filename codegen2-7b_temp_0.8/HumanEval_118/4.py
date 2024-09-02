
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
    if len(word) <= 1:
        return ""
    else:
        vowels = ["a","e","i","o","u","y","A","E","I","O","U","Y"]
        vowels_count = { vowel: vowel.count("a") for vowel in vowels }
        word_list = word.split()
        left_vowels = word_list[-1].count("a")
        right_vowels = word_list[0].count("a")
        closest_vowel = ""
        if (left_vowels >= right_vowels):
            closest_vowel = vowels[0]
        return closest_v
