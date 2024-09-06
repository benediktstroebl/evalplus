
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    #Check if all letters are vowels
    if all(i.lower() in vowels for i in word):
        return ''
    #Check if word has a vowel
    for i in range(len(word) - 1):
        if word[i].lower() in vowels and word[i + 1].lower() not in vowels:
            return word[i].lower()


    #Check if all letters are consonants
    if all(i.lower() not in vowels for i in word):
        return ''
    #Check if word has a consonant
    for i in range(len(word) - 1):
        if word[i].lower() not in vowels and word[i + 1].lower() in vowels:
            return word[i + 1].lower()




    return ''

