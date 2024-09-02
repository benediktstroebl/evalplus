
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
    # convert the word to lowercase and split it into a list of words
    words = word.lower().split()
    
    # initialize a variable to store the closest vowel
    closest_vowel = ""
    
    # iterate through the words and check if any vowel is in the right side of the word
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[j] in "aeiouAEIOU" and j > i:
                closest_vowel = words[j]
                break
        if closest_vowel:
            break
    
    return closest_vowel