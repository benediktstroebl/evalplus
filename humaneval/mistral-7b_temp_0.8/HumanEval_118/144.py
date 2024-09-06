
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

    # only a, e, i, o, u count as vowels
    vowels = 'aeiou'

    # make word lowercase
    word = word.lower()

    # if no vowels are found
    if not vowels.count(word[0]) and not vowels.count(word[-1]):
        return ''
    elif vowels.count(word[0]):
        # if only vowels are in the beginning, no vowels are in the middle
        if not vowels.count(word[1:]):
            return ''
        else:
            # find the index of the vowel after the first vowel
            for index, letter in enumerate(word):
                if letter in vowels and index > 0:
                    return word[index]
    elif vowels.count(word[-1]):
        # if only vowels are in the ending, no vowels are in the middle
        if not vowels.count(word[:-1]):
            return ''
        else
