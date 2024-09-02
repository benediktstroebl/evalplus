
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
    start = 0
    end = 0
    for i in range(len(word)):
        if word[i] == 'c' or word[i] == 's':
            end = i
        elif word[i] == 'a' or word[i] == 'o' or word[i] == 'u':
            start = i
    return word[start:end+1] if start < len(word) - 1 else ""
