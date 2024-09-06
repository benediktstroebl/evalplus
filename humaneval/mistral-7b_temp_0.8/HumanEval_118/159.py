
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
    word_ = word.lower()
    vowels = 'aeiou'
    vowel_index = ''
    consonant_index = ''
    i = 0
    while word_[i] != '':
        if word_[i] in vowels:
            vowel_index = i
        elif word_[i] in 'bcdfghjklmnpqrstvwxyz':
            consonant_index = i
        i += 1

    if vowel_index != '' and consonant_index != '':
        return word_[vowel_index]
    else:
        return ''
