
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
    
    # find the index of first vowel
    # e.g. "dw" -> 2
    # e.g. "w" -> 0
    index = -1
    for i in range(len(word)-1):
        if word[i] in 'aeiou':
            index = i
            break

    # if index == -1, return empty string
    if index == -1:
        return ''

    # if there is only one vowel left, return vowel
    if len(word) - index == 1:
        return word[index]

    # if there is only one vowel left, return vowel
    if len(word) - index == 2:
        return word[index+1]

    # find the index of the second vowel
    last_index = len(word)-1
    for i in range(len(word)-1, -1, -1):
        if word[i] in 'aeiou':
            last_index = i
            break
    
    # check if there is no consonant between index and last index
    if index < last_index and word[index+1] not in 'aeiou':
        return word[index]

    # check if there is no consonant between index and last index
    if index < last_index and word[index+1] in 'aeiou':
        return word[index+1]

    # if neither of the condition is met, return the vowel between index and last index
    return word[index+1]

