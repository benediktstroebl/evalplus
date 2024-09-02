
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
    c1 = 'aeiou'
    c2 = 'aeiou'
    vowels = 'aeiou'
    for i in range(len(word)):
        if word[i] in c1:
            c1 = c1.replace(word[i], '')
        else:
            c2 = c2.replace(word[i], '')
            break
    if c1:
        vowels = vowels + c1
    if c2:
        vowels = vowels + c2
    return vowels if vowels in vowels else ''
