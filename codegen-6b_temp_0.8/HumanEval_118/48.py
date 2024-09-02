
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
    if len(word) == 0:
        return ''
    if len(word) == 1:
        if word[0].lower() in "aeiou":
            return word[0]

    word = word.lower()

    if word[-1] in "aeiou":
        return word[-1]
    elif word[-2] in "aeiou":
        if word[-1] == word[-2]:
            return word[-1]
        else:
            return ''
    else:
        return ''


