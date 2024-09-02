
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
    index = 0
    for char in word:
        if char in vowels:
            if index == 0 or index == len(word) - 1:
                return ""
            if word[index - 1].isalpha() and word[index - 1].lower() != word[index].lower():
                return word[index - 1]
            if word[index + 1].isalpha() and word[index + 1].lower() != word[index].lower():
                return word[index + 1]
        index += 1
    return ""
