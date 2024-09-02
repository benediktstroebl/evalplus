
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
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'
    for i in word:
        if i in consonants and i != word[0] and i != word[-1]:
            if word[word.index(i) + 1] in vowels or word[word.index(i) - 1] in vowels:
                return i
    return ''

