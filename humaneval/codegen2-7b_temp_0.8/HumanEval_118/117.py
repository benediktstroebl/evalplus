
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
    vowel_count = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    consonants = set(string.ascii_lowercase)
    for c in word:
        if c in consonants:
            vowel_count[c] += 1
            consonants.remove(c)
    vowel = ""
    for c, count in vowel_count.items():
        if count > 0:
            vowel = c
            break
    return vowel



