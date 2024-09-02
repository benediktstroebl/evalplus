
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
    # remove all special characters and whitespace
    word = word.translate(str.maketrans('', '', string.punctuation))
    # split the word into a list of characters
    word_chars = word.split
    # initialize position of the first character to (0, 0)
    first_char_pos = (0, 0)
    # iterate through the characters
    for i in range(len(word_chars)):
        # check if the character is a vowel
        if word_chars[i].lower() in "aeiou":
            # calculate the distance between the first character and the current character
            char_pos = (first_char_pos[0] + 1, first_char_pos[1])
            # update the position of the first character if this character is closer
            if abs(char_pos[0] - i) < abs(char_pos[0] - len(word_chars)):
                first_char_pos = char_pos
            # if this is the closest vowel, return it
            if len(word) >= 2 and first_char_pos[0] == 0:
                return first_char_pos[1]
        # update the position of the first character
        first_char_pos = (i, 0)
    # if no vowel was found, return an empty string
    return ""
