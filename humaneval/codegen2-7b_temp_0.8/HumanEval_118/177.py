
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    word_len = len(word)

    if word_len < 3:
        return ""
    if word[0] not in vowels or word[word_len-1] not in vowels:
        return ""

    vowel_index = word.rindex(vowels[1])
    consonant_index = word.rindex(vowels[0])
    
    if vowel_index - consonant_index == 1:
        return ""
    else:
        return word[vowel_index + 1 : consonant_index
