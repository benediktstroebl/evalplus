
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
    # convert 'camelCase' to a 'camelCase'
    word = word.lower()
    
    # no vowels found
    if word.count('a') == 0 or word.count('e') == 0 or word.count('i') == 0 or word.count('o') == 0 or word.count('u') == 0:
        return ""
    
    # find the first letter that is not 'a, e, i, o, or u
    for i in range(len(word) - 1, 0, -1):
        if word[i] not in 'aeiou':
            index = i
            break
    
    # find the first 'a', 'e', 'i', 'o', or 'u' after the index that was found
    for i in range(index, len(word)):
        if word[i] in 'aeiou':
            return word[i]
