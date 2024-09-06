
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


    # your code goes here


    a = "a"
    e = "e"
    i = "i"
    o = "o"
    u = "u"
    v = "y"

    word = word.lower()

    if word[-2] == a or word[-2] == e or word[-2] == i or word[-2] == o or word[-2] == u or word[-2] == v:
        return word[-2]
    if word[-3] == a or word[-3] == e or word[-3] == i or word[-3] == o or word[-3] == u or word[-3] == v:
        return word[-3]
    if word[-1] == a or word[-1] == e or word[-1] == i or word[-1] == o or word[-1] == u or word[-1] == v:
        return word[-1]
    if word[-4] == a or word[-4] == e or word[-4] == i or word[-4] == o or word[-4] == u or
