
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

    vowels = set("aeiou")
    word = word.strip()
    consonants = set()
    for idx, char in enumerate(word[::-1]):
        if char.isalpha():
            break
        else:
            consonants.add(char)
    closest_vowel = ""
    for char in word[::-1]:
        if char in vowels:
            closest_vowel = char
            break
        elif char in consonants and closest_vowel:
            break
        else:
            closest_vowel = ""
    if not closest_vowel:
        return closest_vowel
    else:
        return closest_vowel[::-1]
    
