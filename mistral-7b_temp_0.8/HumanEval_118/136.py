
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
    if len(word) == 0:
        return word
    elif not word.isalpha():
        return word
    elif not word.islower():
        return word
    else:
        vowel = ""
        consonant_list = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
        for letter in word:
            if letter in vowel:
                vowel = letter
                break
            elif letter in consonant_list and vowel == "":
                pass
            else:
                return word
        return vowel

    # print("The closest vowel is: {}\n".format(vowel))
    # return vowel

