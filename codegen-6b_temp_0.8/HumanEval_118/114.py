
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
    vowels = ['a', 'e', 'o', 'u']
    if word[0] in vowels:
        return word[0]
    res = []
    for i in range(1, len(word)):
        if word[i] not in vowels:
            res.append(word[i])
        else:
            if word[i] == 'a':
                res.append('e')
            elif word[i] == 'e':
                res.append('a')
            elif word[i] == 'o':
                res.append('u')
            else:
                res.append('u')
    res.append(word[-1])
    return max(res, key=lambda x: abs(ord(x) - ord('a')))

