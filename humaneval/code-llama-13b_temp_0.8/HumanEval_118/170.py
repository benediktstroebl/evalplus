
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
    # The vowels of the alphabet.
    vowels = ['a', 'e', 'i', 'o', 'u']
    # Initialize the result to empty string.
    result = ""
    # Get the length of the word.
    length = len(word)
    # Iterate through the word from the right to the left.
    for i in range(length - 1, 0, -1):
        # If the current character is a vowel and the previous character is a consonant, 
        # set the result to the current character and break the loop.
        if word[i].lower() in vowels and word[i - 1] not in vowels:
            result = word[i]
            break
    return result

