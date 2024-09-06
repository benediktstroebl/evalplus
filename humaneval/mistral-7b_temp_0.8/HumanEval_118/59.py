
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

    #Go through the word backwards 
    #Check if a letter is a vowel
    #If it is a vowel, check if the letter before it is a consonant
    #If it is a consonant, return the vowel
    #If there are no vowels after a consonant, return the empty string
    #return empty string if there are no vowels

    i = len(word) - 1
    while i > 0:
        if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
            if word[i-1] != "a" or word[i-1] != "e" or word[i-1] != "i" or word[i-1] != "o" or word[i-1] != "u":
                return word[i]
        i = i - 1
    return ""

