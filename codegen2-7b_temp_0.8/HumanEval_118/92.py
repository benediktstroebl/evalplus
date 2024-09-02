
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
    
    i = 0
    count = 0
    vowel_count = 0
    
    while i < len(word):
        if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
            vowel_count = vowel_count + 1
        else:
            vowel_count = 0
        if vowel_count == 2:
            count = count + 1
            i = i + 1
        else:
            i = i + 1
    
    if count == 0:
        return ""
    else:
        return word[len(word) - count
