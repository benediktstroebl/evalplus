
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
    # Rules:
    # - Does not start with vowel
    # - Does not end with vowel
    # - closest vowel between two consonants
    # - no vowels between two consonants
    # - no vowels at end of word
    # - closest vowel is the one on the right side
    # - closest vowel is the right most vowel in the word
    # - no vowels at start of word

    # first thing to do is check if the word has any vowels, if it does not we can return an empty string
    if not check_if_vowels_present(word):
        return ""

    # next check if the first and last letters are vowels, if so, check the index
    # of the last letter if it is less than or equal to the index of the second
    # to last letter, remove the first letter, otherwise remove the last letter
    if word[0] in ['a', 'e', 'i', 'o', 'u']:
        if word[len(word) - 1] in ['a', 'e', 'i', 'o', 'u']:
            if word.index(word[len(word) - 1]) <= word.index(word[len(word) - 2]):
                return word.pop(0)
            else:
                return word.pop()
        else:
            return word.pop(0)
    else:
        if word[len(word) - 1] in ['a', 'e', 'i', 'o', 'u']:
            return word.pop()
        else:
            return ""

