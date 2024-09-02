
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
    left_side = ""
    right_side = ""
    for i in range(len(word)-1):
        if word[i] == "c" and word[i+1] == "o":
            if word[i+2] == "n":
                left_side = word[i+2]
            elif word[i+2] == "s":
                right_side = word[i+2]
        elif word[i] == "s" and word[i+1] == "i":
            if word[i+2] == "n":
                left_side = word[i+2]
            elif word[i+2] == "t":
                right_side = word[i+2]
        elif word[i] == "t" and word[i+1] == "a":
            if word[i+2] == "n":
                left_side = word[i+2]
            elif word[i+2] == "r":
                right_side = word[i+2]
        elif word[i] == "p" and word[i+1] == "u":
            if word[i+2] == "e":
                left_side = word[i+2]
            elif word[i+2] == "n":
                right_side = word[i+2]
    if left_side == "e" or left_side == "i" or left_side == "o" or left_side == "u":
        return left_side
    elif right_side == "e" or right_side == "i" or right_side == "o" or right_side == "u":
        return right_side
    else:
        return ""
