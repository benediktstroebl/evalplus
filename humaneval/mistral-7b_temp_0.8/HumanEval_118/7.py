
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
    word = word.lower()
    vowel = "aeiou"
    if "".join([c for c in word if c in vowel and c != word[0] and c != word[-1]]) == "":
        return ""
    else:
        return word.index("".join([c for c in word if c in vowel and c != word[0] and c != word[-1]]))
    # if vowel.index(word[1:-1].lower()) == -1:
    #     return ""
    # else:
    #     return word[1:-1].lower()[vowel.index(word[1:-1].lower())]
