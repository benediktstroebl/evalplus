
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

    vowels = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
    vowels_found = []
    
    for index, char in enumerate(word):
        if char in vowels:
            vowels_found.append((index, char))
    
    if vowels_found == []:
        return ""

    closest_vowel = ""
    min_distance = 100
    
    for index, char in vowels_found:
        distance = index
        if distance < min_distance:
            min_distance = distance
            closest_vowel = char

    return closest_vowel
