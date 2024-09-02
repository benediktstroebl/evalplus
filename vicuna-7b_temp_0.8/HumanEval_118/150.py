
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

    # Replace all consonants with " "
    word = " " + word + " "

    # Split the word with spaces
    word_list = word.split(" ")

    # Initialize empty list to store the closest vowels
    closest_vowels = []

    # Iterate over the list of words
    for word in word_list:

        # Split the word with vowel
        vowel_list = word.split("")

        # Iterate over the vowel list
        for vowel in vowel_list:

            # If the vowel is a consonant
            if "a" <= vowel <= "z" or "A" <= vowel <= "Z":
                continue

            # If the vowel is a space
            if vowel == " ":
                continue

            # If the vowel is a close vowel
            if "i" in vowel or "u" in vowel:
                continue

            # If the vowel is a open vowel
            if "a" in vowel or "e" in vowel:
                # Add the vowel to the closest vowels list
                closest_vowels.append(vowel)

    # Return the closest vowel
    return closest_vowels[0]