
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
    if not word:
        return ""
    
    # sort word so that consonants come first
    word = sorted(word)
    
    # find the index of the first consonant
    first_consonant_index = word.index("c") if "c" in word else word.index("s") if "s" in word else -1
    if first_consonant_index == -1:
        return ""
    
    # find the index of the first vowel
    vowel_index = word.index("a") if "a" in word else word.index("e") if "e" in word else word.index("i") if "i" in word else word.index("o") if "o" in word else word.index("u") if "u" in word else -1
    if vowel_index == -1:
        return ""
    
    # calculate the distance between the first vowel and the first consonant
    vowel_index -= first_consonant_index
    
    # check if the closest vowel is the second vowel
    if vowel_index == 0:
        return word[vowel_index+1]
    
    # return the closest vowel
    return word[vowel_index]