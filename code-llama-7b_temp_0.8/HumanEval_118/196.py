
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

    last_consonant_index = len(word) - 1

    while last_consonant_index > 0:
        last_consonant_index -= 1
        if word[last_consonant_index].isalpha():
            break

    while last_consonant_index < len(word) - 1:
        if word[last_consonant_index].isalpha():
            break
        last_consonant_index += 1

    vowels = ("A","E","I","O","U")

    if last_consonant_index + 1 >= len(word):
        return ""

    return word[last_consonant_index] if word[last_consonant_index+1] in vowels else word[last_consonant_index+1]
    

