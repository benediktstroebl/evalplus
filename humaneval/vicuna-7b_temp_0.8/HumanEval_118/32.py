
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
    previous_index = 0
    previous_char = word[previous_index]
    current_index = len(word) - 1
    current_char = word[current_index]
    while previous_char not in "rnmtks" and current_char not in "rnmtks":
        if previous_char == " ":
            previous_index += 1
            if previous_index == len(word):
                return ""
            previous_char = word[previous_index]
        elif previous_char == current_char:
            if current_char == " ":
                current_index -= 1
                if current_index < 0:
                    return ""
                current_char = word[current_index]
            else:
                return ""
        else:
            return ""
    return previous_char