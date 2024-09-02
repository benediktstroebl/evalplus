
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
    # from prof
    vowels = ('a', 'e', 'i', 'o', 'u')

    def get_min_dist(var, lit):
        """Minimal distance of var to lit from right side.
        """
        return min((abs(var - lit), lit))

    for i, c in reversed(list(enumerate(word))):
        if c in vowels:
            return word[i+1:]
    return ""

