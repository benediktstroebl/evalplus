
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
    vowels = ["a", "e", "i", "o", "u"]
    word = list(word)
    # print(word)
    a = word.index(word[0])
    b = word.index(word[-1])
    # print(a, b)
    i = a
    while a < b:
        # print(i, a, b)
        if word[i] in vowels:
            return word[i]
            # break
        i += 1
        a += 1
