
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

    import re
    consonant_pattern = '[^a-zA-Z]'
    word = word[::-1]
    regex_pattern = '(([^aeiou]{2}|[^aeiou]{1}[^aeiou])[aeiou])'

    for match in re.finditer(regex_pattern, word):
        vowel = match.group(1)
        return vowel[::-1]
    return ''
