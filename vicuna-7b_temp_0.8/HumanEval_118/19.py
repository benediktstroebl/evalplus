
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
    if len(word) < 2:
        return ""
    left_side = re.search(r'[aeiouAEIOU]', word)
    right_side = re.search(r'[bdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', word, re.DOTALL)
    if not left_side and not right_side:
        return ""
    if left_side and right_side:
        if left_side.end() < right_side.start():
            return left_side.group(0)
        else:
            return ""
    return left_side.group(0)
