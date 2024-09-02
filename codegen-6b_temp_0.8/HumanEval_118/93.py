
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
    # Your code here
    # return ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    i, j = len(word) - 1, len(word) - 1

    while i >= 0 and j >= 0 and word[i] not in vowels:
        i -= 1

    while j >= 0 and word[j] not in vowels:
        j -= 1

    if i >= 0 and j >= 0:
        return word[j + 1]

    return word[i + 1]

