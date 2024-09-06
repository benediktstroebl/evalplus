
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

    closest = ''
    i = -1
    while True:
        i = word.find('c', i + 1)
        if i == -1:
            break
        j = word.find('c', i + 1)
        if j!= -1:
            break
    if i == -1:
        return ''
    while True:
        if word[i] in "AEIOU":
            closest = word[i]
            break
        i = word.find('c', i + 1)
        if i == -1:
            break
    return closest
