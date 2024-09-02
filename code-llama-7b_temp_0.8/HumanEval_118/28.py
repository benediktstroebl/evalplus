
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
    # Check the length of the word
    if len(word) == 1:
        return ""

    # Move the pointer to the end of the string and minus 2
    pointer = len(word) - 2
    
    # Check if the last two letters are vowels or consonants
    if word[pointer] in ['a', 'e', 'i', 'o', 'u']:
        return word[pointer]
    elif word[pointer + 1] in ['a', 'e', 'i', 'o', 'u']:
        return word[pointer + 1]
    else:
        # Move the pointer to the left until it's vowel or it's the beginning
        while pointer >= 0 and word[pointer] not in ['a', 'e', 'i', 'o', 'u']:
            pointer -= 1

        if pointer < 0:
            return ""
        else:
            return word[pointer]

