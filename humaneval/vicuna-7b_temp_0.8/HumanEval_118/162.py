
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

    # initialize string to store the result
    result = ""

    # check if the word is empty
    if not word:
        return result

    # check if the word only contains consonants
    consonants = True
    for char in word:
        if not char.isalpha():
            consonants = False
            break

    # if the word only contains consonants, return empty string
    if consonants:
        return result

    # check if the word starts with a vowel
    if word[0].isalpha() and word[0].lower() in "aeiouAEIOU":
        result = word[0].lower()
        word = word[1:]

    # check if the word ends with a vowel
    for char in reversed(word):
        if char.isalpha() and char.lower() in "aeiouAEIOU":
            result = word[::-1][0].lower()
            break

    # if there are no vowels after the word, return empty string
    if not result:
        return ""

    # find the closest vowel
    vowels = "aeiouAEIOU"
    i = 0
    while i < len(vowels) - 1:
        j = i + 1
        while j < len(vowels) and vowels[j].lower() > result.lower():
            j += 1
        if j == len(vowels):
            break
        if vowels[i].lower() <= result.lower():
            break
        i = j

    # return the closest vowel
    return vowels[i].lower()
