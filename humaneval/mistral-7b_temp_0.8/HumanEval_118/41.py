
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
    words = list(word)
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    for idx in range(1, len(words)-1):
        if words[idx] in vowels:
            vowel_count += 1
    if vowel_count != 0:
        return words[words.index(words[idx-1], idx, len(words))]
    else:
        return ""
