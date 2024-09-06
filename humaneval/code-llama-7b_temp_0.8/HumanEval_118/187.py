
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
    if len(word) < 3:
        return ""
    last_consonant_index = len(word) - 1
    for i in range(last_consonant_index, 0, -1):
        if word[i].lower() in "aeiou":
            if i < last_consonant_index:
                if word[i + 1].lower() in "aeiou":
                    return word[i]
            return word[i]
    return ""

