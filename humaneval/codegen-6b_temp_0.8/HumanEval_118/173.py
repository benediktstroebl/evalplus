
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
    vowels = "aeiou"
    # Any other characters
    others = "".join(set(word) - set(vowels))
    # Refer to the vowel_positions array for the mapping of other characters to the closest vowel
    vowel_positions = [word.rfind(vowel) for vowel in vowels]
    # Get the max index among the vp array
    max_index = max(vowel_positions)
    # Return the char at the max index if the char is among the others
    if max_index < len(word):
        return word[max_index]
    else:
        # Return the char at the max index if the char is among the others
        return word[vowel_positions.index(max_index)]
