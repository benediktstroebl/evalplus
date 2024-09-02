
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
    # remove all non-alphanumeric characters
    word = "".join(word for word in word if word.isalnum())
    
    # split the string into words
    words = word.split(" ")
    
    # initialize counter for vowel and consonants
    vowel_counter = 0
    consonant_counter = 0
    
    for word in words:
        if word.startswith(" ":x):
            vowel_counter += 1
            continue
        if word.endswith(" "):
            consonant_counter += 1
            continue
        if word.isalpha():
            vowel_counter += 1
            consonant_counter += 1
    
    # if no vowel found return empty string
    if vowel_counter == 0:
        return ""
    
    # find the closest vowel
    closest_vowel = max(set(word.split("")[1:vowel_counter])-set(word.split("")[:vowel_counter]))
    
    # if no vowel found return empty string
    if closest_vowel == "" or closest_vowel == word[0]:
        return ""
    
    return closest_vowel