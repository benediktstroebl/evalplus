
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

    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    index = len(word)
    vowel_index = -1
    vowel = ""

    while index >= 0:
        if word[index] in vowels:
            vowel_index = index
            vowel = word[index]
        if word[index] not in vowels:
            index -= 1
        else:
            if index > vowel_index:
                vowel = word[index]
                break
            else:
                break

    if vowel == "":
        return ""

    # index = vowel_index
    consonant = ""
    index += 1

    while index < len(word):
        if word[index] in vowels:
            consonant = ""
            break
        if word[index] not in vowels:
            consonant = word[index]
        index += 1
    
    if consonant == "":
        return ""

    return vowel
