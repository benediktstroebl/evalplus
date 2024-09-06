
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
    vowels = "aeiouyAEIOUY"
    vowels_in_word = [c for c in word if c in vowels]
    
    if len(vowels_in_word) <= 1:
        return ''
    
    # get last two vowels in the word
    last_two_vowels = vowels_in_word[-2:]
    index = len(word) - len(last_two_vowels)
    print(index)
    
    for c in word[index:]:
        if c in vowels:
            return c

    return ''


