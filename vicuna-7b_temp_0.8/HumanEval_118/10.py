
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
    # check the length of the word
    if len(word) < 2:
        return ""

    # split the word into a list
    words = word.split()

    # initialize variable to keep track of closest vowel
    closest_vowel = ""

    for i in range(len(words)):
        # check the vowel before the current index
        if words[i-1] in "aeiouAEIOU":
            vowel_distance = distance(words[i], words[i-1])
            if vowel_distance < max_distance:
                max_distance = vowel_distance
                closest_vowel = words[i]
        # check the vowel after the current index
        if words[i+1] in "aeiouAEIOU":
            vowel_distance = distance(words[i], words[i+1])
            if vowel_distance < max_distance:
                max_distance = vowel_distance
                closest_vowel = words[i+1]

    # check if we found any vowel
    if closest_vowel == "":
        return ""

    return closest_vowel
