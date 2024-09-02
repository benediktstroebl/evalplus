
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    consonants = ''
    for i in word:
        if i.isalpha():
            consonants += i
        else:
            consonants = consonants[:-1]
            return ""

    min = len(word)
    for i in vowels:
        consonants = consonants[:-1]
        if (consonants + i in word):
            if min > len(word):
                min = len(word)
            return i

    return ""


