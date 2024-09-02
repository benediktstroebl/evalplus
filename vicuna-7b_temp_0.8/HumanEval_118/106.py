
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
    # get all the letters in the word
    word_letters = word.lower().split()
    
    # find the index of the first and last consonants
    first_consonant = 0
    last_consonant = len(word_letters) - 1
    
    # find the index of the last vowel
    vowel_index = -1
    
    # loop through the letters
    for i in range(1, len(word_letters)):
        if word_letters[i].isalpha() and word_letters[i].isupper() and word_letters[i - 1].isalpha() and word_letters[i - 1].islower():
            first_consonant = i
        elif word_letters[i].isalpha() and word_letters[i].islower() and word_letters[i - 1].isalpha() and word_letters[i - 1].isupper():
            last_consonant = i
            
        # check if the current letter is a vowel
        if word_letters[i].isalpha() and word_letters[i].isupper() and word_letters[i - 1].isalpha() and word_letters[i - 1].islower():
            vowel_index = i - 1
        
    # check if the vowel is closer to the right side
    if vowel_index > 0 and (word_letters[vowel_index] - word_letters[last_consonant]) > (word_letters[vowel_index] - word_letters[first_consonant]):
        return word_letters[vowel_index]
    
    # if there is no vowel or no consonant on the right side
    if vowel_index == -1 or last_consonant == len(word_letters) - 1:
        return ""
    
    # if there is no vowel closer to the right side
    if (word_letters[vowel_index] - word_letters[last_consonant]) <= (word_letters[vowel_index] - word_letters[
