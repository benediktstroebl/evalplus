
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
    word = word.strip()
    if len(word) < 2:
        return ""
    right_letter = word[-1]
    left_letter = word[-2]

    # if last letter is a vowel, the only one closest vowel is the last vowel
    if left_letter in vowels:
        return left_letter
    elif right_letter in vowels:
        return right_letter
    else:
        for v in vowels:
            if left_letter == v or right_letter == v:
                return v
    return ""
    
