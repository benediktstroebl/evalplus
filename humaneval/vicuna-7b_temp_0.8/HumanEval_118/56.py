
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
    vowels = "aeiou"
    previous_char = ""
    current_char = ""
    previous_word = ""
    index = 0
    while index < len(word) - 1:
        if word[index] in vowels and word[index+1] not in vowels:
            if previous_char == " ":
                return current_char
            elif previous_char == word[index]:
                return ""
            else:
                previous_char = word[index]
                current_char = word[index+1]
        index += 1
    return ""
