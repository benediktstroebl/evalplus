
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
    word = word.lower()
    vowels = "aeiouAEIOU"
    prev_char = ""
    for char in word:
        if char.lower() not in vowels:
            if prev_char.lower() == char.lower():
                if char.lower() == "y":
                    if prev_char.lower() == "r":
                        return "y"
                    elif prev_char.lower() == "s":
                        return "y"
                elif prev_char.lower() == "b":
                    if char.lower() == "l":
                        return "b"
                    elif char.lower() == "p":
                        return "b"
                elif prev_char.lower() == "t":
                    if char.lower() == "a":
                        return "t"
                    elif char.lower() == "n":
                        return "t"
                elif prev_char.lower() == "d":
                    if char.lower() == "g":
                        return "d"
                    elif char.lower() == "n":
                        return "d"
            prev_char = char.lower()
    return ""
