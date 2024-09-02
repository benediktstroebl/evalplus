
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
    # check if the word is empty
    if not word:
        return ""
    
    # split the word into a list
    words = word.split()
    
    # check if the word is empty
    if not words:
        return ""
    
    # initialize the index and the distance to the closest vowel
    index = 0
    distance = 0
    
    # check each letter
    for i in range(len(words)):
        # check the current letter
        if words[i].isalpha():
            # check if the letter is a vowel
            if words[i].isvowel():
                # get the distance between the current letter and the closest vowel
                if i > index:
                    distance = len(words[i].lower()) + len(words[index].lower())
                # update the index and the distance
                index = i
                distance = len(words[i].lower())
            else:
                # update the distance
                distance += len(words[i].lower())
    
    # return the closest vowel
    return words[index].lower()
