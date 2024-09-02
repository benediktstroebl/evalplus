
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
    vowels = {'a' : 0, 'e' : 1, 'i' : 2, 'o' : 3, 'u' : 4}
    if word[0] in vowels:
        index = 0
    else:
        index = 1
    for i in range(1, len(word)):
        if word[i] in vowels:
            if word[i-1] in vowels:
                return word[i]
            else:
                return word[i-1]
    return word[index]
