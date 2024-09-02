
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
    result = ""
    if len(word) > 2:
        i = len(word) - 1
        while i > 1:
            if (word[i].lower() in "aeiou" and word[i-1].lower() != word[i].lower() and word[i-2].lower() != word[i].lower()) or (word[i].lower() in "aeiou" and word[i-1].lower() == word[i].lower() and word[i-2].lower() != word[i].lower()):
                result = word[i]
                break
            else:
                i -= 1
    return result
