
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

    # get indexes of first and last vowels
    first_index = -1
    last_index = -1
    for i in range(len(word)):
        if word[i] in 'aeiou':
            if first_index == -1:
                first_index = i
            last_index = i
    # check if we have found any vowels
    if first_index == -1 or last_index == -1:
        return ''
    # move first_index to the right and last_index to the left
    while first_index < last_index:
        first_index += 1
        last_index -= 1
    # check if any consonant between them is vowel
    if word[first_index] in 'aeiou' or word[last_index] in 'aeiou':
        return ''
    else:
        return word[first_index]

