
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
    # Check if the first or last characters are vowels and remove them
    if len(word) > 2 and word[-1] in "aeiouAEIOU":
        word = word[:-1]
    if len(word) > 2 and word[0] in "aeiouAEIOU":
        word = word[1:]
        
    # If the remaining string is less than 2, return an empty string
    if len(word) < 2:
        return ""
    
    # Reverse the string and find the first vowel
    reversed_word = word[::-1]
    vowel = next((x for x in reversed_word if x in "aeiouAEIOU"), None)
    
    # If no vowel was found, return an empty string
    if not vowel:
        return ""
    
    # Find the index of the vowel and subtract it from the length of the string to get the
    # index of the vowel in the original string
    index = reversed_word.index(vowel)
    return word[-(index + 1)]
    
    
