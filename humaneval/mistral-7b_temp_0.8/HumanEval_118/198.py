
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
    word = word.lower()

    if not word or not vowels:
        return ""

    if all(not(letter in vowels) for letter in word):
        return ""

    stack = []
    for letter in word:
        if letter in vowels:
            stack.append(letter)
        elif stack:
            return stack.pop()

    return stack.pop()

