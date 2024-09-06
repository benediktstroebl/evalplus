
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
    def check(word, ind, ind_vowel):
        if ind >= len(word):
            return ind_vowel
        return (word[ind] in vowels) and check(word, ind + 1, ind) or check(word, ind + 1, ind_vowel)

    return ''.join(filter(lambda ch: check(word, 0, ch), vowels))

