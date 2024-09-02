
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
    if len(word) < 2:
        return ""
    last_consonant = word.rindex("n") if word.endswith("n") else word.rindex("l") if word.endswith("l") else -1
    if last_consonant == -1:
        return ""
    before_last_consonant = word[:last_consonant]
    if any(c.lower() in "aeiou" for c in word):
        return word[last_consonant+1:].split("")[0]
    else:
        return ""
