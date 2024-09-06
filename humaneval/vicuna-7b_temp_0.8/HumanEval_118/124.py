
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
    vowels = set(string.ascii_letters) - set(string.punctuation)
    half_word = len(word)//2
    vowel_idx = vowels.index(word[half_word+1]) if half_word != -1 else vowels.index(word[0])
    if vowel_idx != -1:
        return word[half_word:vowel_idx+1] if vowel_idx < len(word) - 1 else ""
    else:
        return ""
