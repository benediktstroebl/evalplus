
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
    consonants = [char for char in word if char not in vowels]
    vowel_found = False
    i = 0
    while not vowel_found and i < len(consonants) - 1:
        if consonants[i] not in vowels and consonants[i+1] in vowels:
            vowel_found = True
        else:
            i += 1
    return vowels[i] if vowel_found else ''

