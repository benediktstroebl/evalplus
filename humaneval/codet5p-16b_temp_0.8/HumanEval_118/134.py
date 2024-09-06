
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

    closest_vowel = ""
    
    for i, letter in enumerate(word[::-1]):
        if letter not in "aeiou":
            continue
        
        left_consonant = word[::-1][i+1:]
        if left_consonant.replace(letter, "").replace(left_consonant[0], "")!= "" and \
                left_consonant.replace(left_consonant[0], "").replace(left_consonant[0], "") in "aeiou":
            closest_vowel = letter
            break

    return closest_vowel

