
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
    # Your code here
    vowel = "aeiouy"
    if len(word) <= 1:
        return ""
    word_reversed = word[::-1]
    if word[0] in vowel or word[0] in vowel.upper():
        word_reversed = word_reversed[1:]
    if word[len(word) - 1] in vowel or word[len(word) - 1] in vowel.upper():
        word_reversed = word_reversed[:-1]
    for i in range(len(word_reversed)):
        if word_reversed[i] in vowel or word_reversed[i] in vowel.upper():
            return word_reversed[i - 1]
    return ""
