
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

    def check_vowel(c):
        return c.lower() in 'aeiou'

    def check_between(c1, c2):
        return c2.lower() not in 'aeiou' and c1.lower() not in 'aeiou'

    def get_vowel(word):
        for i in range(len(word)-1, -1, -1):
            if check_vowel(word[i]):
                return word[i]
        return ''

    if not word:
        return ''

    vowel = get_vowel(word)
    if not vowel:
        return ''

    for i in range(len(word)-1, -1, -1):
        if check_between(word[i], vowel):
            return word[i]

    return ''

