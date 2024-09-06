
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
    # convert the word to lowercase
    word = word.lower()
    # remove all spaces and punctuations
    word = word.translate(str.maketrans("", "", string.punctuation))
    # split the word into a list of characters
    word_chars = word.split()
    # sort the list of characters
    word_chars.sort()
    # get the index of the first vowel in the sorted list
    first_vowel_idx = word_chars.index("aeiou")
    # get the index of the closest vowel
    closest_vowel_idx = first_vowel_idx - 1
    # check if the closest vowel is in the right position
    if closest_vowel_idx >= 0:
        return word_chars[closest_vowel_idx]
    else:
        return ""