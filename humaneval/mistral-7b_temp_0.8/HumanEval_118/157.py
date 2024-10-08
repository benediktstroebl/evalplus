
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
    # your code goes here
    vowel = 'aeiou'
    vowel_pos = []
    vowel_pos = [i for i in range(len(word)) if word[i] in vowel]
    vowel_pos = vowel_pos[1:]
    if len(vowel_pos) != 0:
        vowel_pos = vowel_pos[0]
    else:
        vowel_pos = ''
    return vowel_pos
