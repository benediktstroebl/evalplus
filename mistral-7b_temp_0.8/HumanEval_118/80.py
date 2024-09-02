
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
    new_word = word.lower()
    new_word = new_word.replace("a", "*")
    new_word = new_word.replace("e", "*")
    new_word = new_word.replace("i", "*")
    new_word = new_word.replace("o", "*")
    new_word = new_word.replace("u", "*")
    # print(new_word)
    if new_word == "":
        return ""
    else:
        return new_word[new_word.index("*")-1]


