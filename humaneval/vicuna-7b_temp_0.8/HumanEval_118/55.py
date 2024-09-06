
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
    vowel_list = "aeiou"
    i = len(word) - 1
    while i >= 0:
        j = len(word) - 2 if i == len(word) - 1 else len(word) - 1 - i
        if word[i] == word[j] and word[i+1] in vowel_list and \
           (vowel_list.index(word[i+1]) + 1) % 2 == 0:
            return word[i]
        i, j = j, i
    return ""
