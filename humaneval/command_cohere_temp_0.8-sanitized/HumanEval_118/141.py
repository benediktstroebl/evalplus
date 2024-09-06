def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that 
    stands between two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending don't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    # using regex to check right boundary
    match = word.rstrip('Q')
    if match:
        return 'u'
    match = word.rstrip('q')
    if match:
        return 'u'
    match = word.rstrip('Z')
    if match:
        return 'a'
    match = word.rstrip('z')
    if match:
        return 'a'
    match = word.rstrip('S')
    if match:
        return 'a'
    match = word.rstrip('s')
    if match:
        return 'a'
    match = word.rstrip('L')
    if match:
        return 'e'
    match = word.rstrip('l')
    if match:
        return 'e'
    match = word.rstrip('R')
    if match:
        return 'o'
    match = word.rstrip('r')
    if match:
        return 'o'
    return ''