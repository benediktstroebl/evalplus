
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
    
    current = word[0]
    vowels = ("a", "e", "i", "o", "u")
    for i in range(1, len(word)):
        vowel_distance = float("inf")
        letter = word[i]
        if letter in vowels:
            vowel_distance = min(abs(ord(current) - ord(letter)), vowel_distance)
        current = letter
    
    return word[0] if vowel_distance == float('inf') else word[0] + word[vowel_distance:]
