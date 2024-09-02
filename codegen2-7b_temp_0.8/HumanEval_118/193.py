
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
    vowels = ["a","e","i","o","u"]
    for vowel in word:
        if vowel not in vowels:
            return ""
    for index in range(len(word)):
        if word[index] not in vowels:
            vowels.append(word[index])
    vowels.sort()
    left_consonant = word[0]
    right_consonant = word[-1]
    for vowel in vowels:
        if vowel < left_consonant and vowel > right_consonant:
            return vowel
    
