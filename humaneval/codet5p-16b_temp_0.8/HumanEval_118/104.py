
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

    vowels = 'aeiou'
    consonants = 'qwrtypsdfghjklzxcvbnm'
    if len(word) < 3:
        return ''
    closest_vowel = ''
    left_consonant = True
    for i in range(len(word) - 1, -1, -1):
        letter = word[i]
        if left_consonant:
            if letter in vowels:
                closest_vowel = letter
                left_consonant = False
            elif letter in consonants:
                closest_vowel = closest_vowel[::-1]
                left_consonant = False
            else:
                left_consonant = False
        else:
            if letter in vowels:
                closest_vowel = letter
                left_consonant = True
            else:
                closest_vowel = closest_vowel[::-1]
                return closest_vowel


