
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

    def is_consonant(c):
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            return False
        return True
    index = -1
    res = ""
    for i in range(len(word)-1, -1, -1):
        if is_consonant(word[i]) and is_consonant(word[i-1]) and word[i-1] != word[i-2] and word[i] != word[i+1]:
            index = i
            break
    if index == -1:
        return ""
    for i in range(index, len(word), 1):
        if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
            res = word[i]
            break
    return res
