
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
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels_index = [vowels.find(v) for v in vowels]
    consonants_index = [consonants.find(c) for c in consonants]
    word_index = [word.find(char) for char in word]
    if not word_index:
        return ''
    elif not set(word_index).intersection(vowels_index):
        return ''
    else:
        return word[word_index.index(min(vowels_index))]

    return
