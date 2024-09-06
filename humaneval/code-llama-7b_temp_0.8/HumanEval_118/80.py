
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
    def _get_closest_vowel(word, i):
        """Get the closest vowel from right side of word[i:]"""
        for j in range(i + 1, len(word)):
            if word[j].lower() in "aeiouy":
                return word[j]
        return ""
    
    i = 0
    while i < len(word):
        if word[i].lower() in "aeiouy":
            i += 1
        else:
            return _get_closest_vowel(word, i)
    return ""




