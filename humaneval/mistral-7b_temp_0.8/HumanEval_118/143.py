
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
    vowels = ['a','e','i','o','u']
    word = word.lower()
    for x in word:
        if x in vowels:
            if x == word[0] or x == word[-1]:
                return ""
            if x == word[-2] or x == word[-3]:
                return ""
            for y in word[1:-1]:
                if x == y:
                    return ""
            return x
    return ""





