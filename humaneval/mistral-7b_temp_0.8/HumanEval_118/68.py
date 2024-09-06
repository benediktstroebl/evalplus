
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

    # List of vowels
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    # Initialize the closest_vowel variable
    closest_vowel = ""
    # Initialize the counter variable to keep track of the count of consonants
    counter = 0
    for char in word:
        if char.isalpha():
            if char in vowels:
                closest_vowel = char
                break
            elif char.isupper():
                counter += 1
            else:
                counter -= 1

    # Check if any vowel was found
    if closest_vowel:
        return closest_vowel
    else:
        return ""

