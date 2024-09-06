
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
    if word == "":
        return ""
    else:
        last_char = word[-1]
        return_vowel = ""
        if last_char in "AEIOUY":
            for index in range(len(word) - 1, 0, -1):
                current_char = word[index]
                prev_char = word[index - 1]
                if ord(prev_char) < ord(current_char):
                    return_vowel = prev_char
                    break

        return return_vowel
