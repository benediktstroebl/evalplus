
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
    vowels = "aeiou"
    words = list(word)
    words.reverse()
    for i in range(len(words)):
        if words[i] in vowels:
            if i+1 < len(words) and words[i+1] in vowels:
                continue
            if i-1 >= 0 and words[i-1] in vowels:
                continue
            return words[i]
    return ""



