
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
    word = word.lower()
    i = len(word) - 1
    while i > 0:
        if word[i] in vowels:
            break
        i -= 1
    vowel = word[i]
    if i == 0 or i == len(word) - 1:
        return ""
    vowels.remove(vowel)
    for i in range(i+1, len(word)):
        if word[i] in vowels:
            return word[i]
    return ""
