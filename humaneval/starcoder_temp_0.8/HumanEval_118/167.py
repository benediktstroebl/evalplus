
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

    vowels = "aeiou"
    vowel_positions = []
    for i in range(0, len(word)):
        if word[i] in vowels:
            vowel_positions.append(i)

    if not vowel_positions:
        return ""

    closest_vowel = word[max(vowel_positions)]
    for pos in vowel_positions:
        if abs(pos - max(vowel_positions)) < abs(pos - min(vowel_positions)):
            closest_vowel = word[pos]
            break
    return closest_vowel
