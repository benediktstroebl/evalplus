
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    start = 0
    end = len(word) - 1
    while start < end:
        while word[start] not in vowels:
            start += 1
        while word[end] not in vowels:
            end -= 1
        if word[start] != word[end]:
            return word[end]
        start += 1
        end -= 1
    return ""
