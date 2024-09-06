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
    # Use a dictionary to check if next char to right is a consonant
    char_dict = {
        'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1
        }
    # Find length of the word
    length = len(word)
    # Initialize empty string to store the closest vowel
    closest_vowel = ""
    # Look at the last vowel and check if it is not the last character
    for i in range(length - 1, -1, -1):
        if word[i] in char_dict and word[i + 1] not in char_dict:
            # Update closest vowel if this vowel is closer to the right side
            if abs(i - length) < abs(closest_vowel - length):
                closest_vowel = word[i]
    # Return the closest vowel
    return closest_vowel