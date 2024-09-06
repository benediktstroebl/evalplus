
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
    last = None
    for letter in word[::-1]:
        if letter.lower() in "aeiou":
            last = letter
            break
    tmp = word[::-1]
    for letter in tmp:
        if letter.lower() not in "aeiou":
            tmp = tmp.replace(letter, "", 1)
        else:
            tmp = ""
            break
    if len(word) == 1:
        return ""
    return tmp[::-1] + last

