
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
    index = len(word) - 1
    while index >= 1:
        if word[index].isalpha() and word[index].isupper():
            break
        else:
            index -= 1

    while index < len(word) - 1:
        if word[index + 1].isalpha() and word[index + 1].isupper():
            break
        else:
            index += 1

    for i in range(index, len(word)):
        if word[i] in "AEIOU":
            return word[i]

    return ""

