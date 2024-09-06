
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
    vowels = "aeiouy"
    # get the index of the last vowel
    for i in range(len(word)):
        if word[i].lower() in vowels:
            vowel_index = i
    # if there is no vowel in the word
    if vowel_index == None:
        return ""
    # get the index of the last consonant
    for i in range(len(word)-1, -1, -1):
        if word[i].lower() not in vowels:
            consonant_index = i
    # if the last letter is a vowel
    if consonant_index == len(word)-1:
        return ""
    # return the vowel
    return word[vowel_index + (consonant_index - vowel_index) // 2].lower()
