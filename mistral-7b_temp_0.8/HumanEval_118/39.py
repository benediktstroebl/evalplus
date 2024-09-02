
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
    # your code here
    consonant_list = 'bcdfghjklmnpqrstvwxyz'
    vowel_list = 'aeiou'
    closest_vowel = ''
    last_vowel_index = -1
    first_vowel_index = -1
    last_consonant_index = -1
    word_list = list(word)
    for i in range(len(word_list)):
        if word_list[i] in vowel_list:
            last_vowel_index = i
        if word_list[i] in consonant_list:
            last_consonant_index = i
    for i in range(len(word_list)):
        if word_list[i] in vowel_list:
            first_vowel_index = i
    if (last_vowel_index - last_consonant_index) > 0:
        closest_vowel = word[last_vowel_index - 1]
    elif (first_
