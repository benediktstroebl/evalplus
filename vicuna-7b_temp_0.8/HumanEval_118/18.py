
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
    word = "".join(sorted(word))
    for i in range(len(word) - 2):
        start = i
        end = i + 1
        while start < len(word) and word[start] == word[end] and word[start] in vowels:
            start += 1
        if start == len(word) - 2:
            return ""
    return word[start]
