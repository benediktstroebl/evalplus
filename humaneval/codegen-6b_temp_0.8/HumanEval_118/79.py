
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
    vowels = set('aeiou')
    next_consonant = ''
    for i in range(len(word)-1, -1, -1):
        c = word[i]
        if c in vowels:
            next_consonant = c
            break
    prev_consonant = ''
    for i in range(len(word)-1, -1, -1):
        c = word[i]
        if c in vowels:
            prev_consonant = c
            break
    if next_consonant == '':
        return word[0]
    if prev_consonant == '':
        return word[-1]
    if abs(ord(next_consonant)-ord(prev_consonant)) == 1:
        return prev_consonant
    if abs(ord(next_consonant)-ord(prev_consonant)) == 2:
        if ord(next_consonant)-ord(prev_consonant) > 0:
            return word[i]
        else:
            return word[i-1]
    return ''
