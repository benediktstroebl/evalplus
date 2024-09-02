
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
    vowels = set(string.ascii_letters) - set("bcdfgjklmnopqrstvwxyz")
    start = 0
    end = 0
    closest_vowel = ""
    for i in range(len(word)):
        if word[i] in vowels:
            if i == start:
                if end < len(word) - 1:
                    closest_vowel = word[start:end]
                    start = end
                    end = start + 1
            else:
                start = i
    if start < len(word) - 1:
        closest_vowel = word[start:end]
    return closest_vowel
