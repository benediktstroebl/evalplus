def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that 
    stands between two consonants from the right side of the word (case sensitive).
    Vowels in the beginning and ending doesn't count. 
    Return empty string if you didn't find any vowel met the above condition. 
    You may assume that the given string contains English letter only. 
    """
    # Ensure the word has more than one character to avoid IndexError in the loop.
    if len(word) < 2:
        return ""

    # Use a flag to track whether a potential vowel has been found.
    has_vowel = False

    # Iterate through the letters of the word from right to left, checking for consonants.