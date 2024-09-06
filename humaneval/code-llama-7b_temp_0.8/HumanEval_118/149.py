
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
    vowels = 'AEIOUY'
    if len(word) < 2:
        return ''
    
    # Find the vowel at the end of the word
    def find_vowel(word):
        for i in range(1,len(word)):
            if word[i] in vowels:
                return i
        return None

    # Find the vowel at the beginning of the word
    def find_vowel_before(word):
        for i in range(len(word)-1,0,-1):
            if word[i] in vowels:
                return i
        return None

    # Find the closest vowel in the word
    def find_closest(word):
        for i in range(len(word)-1,0,-1):
            if word[i-1] in vowels and word[i] in vowels:
                return i
        return None

    # If the first vowel is the closest
    if find_vowel_before(word) is None:
        return word[find_vowel(word)]

    # If the last vowel is the closest
    if find_vowel(word) is None:
        return word[find_vowel_before(word)-1]

    # If not, find the closest vowel
    if find_closest(word) is None:
        return ''
    return word[find_closest(word)]




















