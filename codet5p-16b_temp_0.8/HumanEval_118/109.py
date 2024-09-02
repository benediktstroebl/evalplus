
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

    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    i, j = len(word) - 1, len(word)
    while i > 0:
        if word[i] not in vowels:
            i -= 1
        else:
            break
    while j < len(word):
        if word[j] not in vowels:
            j += 1
        else:
            break
    for k in reversed(range(i + 1, j)):
        if word[k] in vowels:
            return word[k]
    return ''

