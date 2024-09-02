
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
    from os.path import expanduser
    import re
    import json

    with open(expanduser("~/Desktop/Python/resources/wordlist.json"), "r") as wordlist:
        dictwords = json.load(wordlist)

    for index, char in enumerate(reversed(word)):
        if not re.match(".*[aeiou].*", word[-index-1:]):
            continue
        else:
            return word[-index-1]

