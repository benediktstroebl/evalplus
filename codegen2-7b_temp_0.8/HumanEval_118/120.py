
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
    vowels = ["a","e","i","o","u","y","A","E","I","O","U","Y"]
    cons = [letter for letter in word if letter not in vowels]
    cons.sort(key = lambda x: x.lower())
    if len(cons) > 0:
        return cons[0]
    else:
        return ""
