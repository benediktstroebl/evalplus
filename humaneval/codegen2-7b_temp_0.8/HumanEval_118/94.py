
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
    vowels = 'aeiouAEIOU'
    i = 0
    j = len(word) - 1
    res = ''
    while i < j:
        if word[i] in vowels and word[j] in vowels:
            res = word[i]
            i += 1
            j -= 1
        elif word[i] not in vowels:
            i += 1
        else:
            j -= 1
    if len(res) == 0:
        return ''
    else:
        return res

