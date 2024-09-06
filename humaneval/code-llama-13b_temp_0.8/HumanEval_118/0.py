
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
    # split word into list of chars
    # reverse it
    # loop through list until first occurance of vowel
    # return that index
    # return empty string if index never found
    # if index is less than 0, return empty string
    # if index is greater than 0, return vowel
    word_list = list(word)
    word_list = word_list[::-1]
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    index = 0
    vowel = ''
    for char in word_list:
        if char in vowels:
            vowel = char
            break
        else:
            index += 1
    if index < 0:
        return ''
    else:
        return vowel


