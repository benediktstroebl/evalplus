
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

    word = word.upper()
    vowels = 'AEIOU'
    vowel_found = False
    last_vowel_index = 0

    for i in range(1, len(word)):
        if word[i] in vowels and word[i - 1] not in vowels and word[i + 1] not in vowels:
            vowel_found = True
            last_vowel_index = i

    if vowel_found:
        return word[last_vowel_index]
    else:
        return ''
















































































































