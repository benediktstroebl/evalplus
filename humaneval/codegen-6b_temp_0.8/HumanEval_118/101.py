
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
    # TODO - you code here
    if word[0].lower() == 'y' or word[-1].lower() == 'y':
        return ''

    vowel = ''
    for symbol in range(1, len(word)):
        if word[symbol].lower() in 'aeiou':
            vowel = word[symbol]
            break

    prev, after = word[-1], word[1]
    if prev.lower() not in 'aeiou':
        prev = ''
    if after.lower() not in 'aeiou':
        after = ''

    return prev + vowel + after
