
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
    # your code goes here
    # if the word contains no consonants, return empty string
    cons = "bcdfghjklmnpqrstvwxz"
    vowel = "aeiou"
    # count the number of consonants and vowels
    count = 0
    vcount = 0
    for i in word:
        if i in cons:
            count += 1
        if i in vowel:
            vcount += 1
    # if the word doesn't have any consonant, return empty string
    if count == 0:
        return ""
    # if there's only one consonant, return the vowel
    if count == 1:
        return vowel[0]
    # if there're two consonants, return the vowel between them
    for i in range(len(word)):
        if word[i] in cons and word[i + 1] in cons:
            return word[i + 1]
    # if there're more than two consonants, return the
