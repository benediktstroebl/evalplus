
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
    vowels = "aeiouAEIOU"
    last_index = len(word) - 1
    closest_vowel = ""
    for index in reversed(range(len(word))):
        for vowel in vowels:
            if word[index] == vowel and word[index+1] == word[index-1]:
                if len(word[index:index+2]) == 3:
                    closest_vowel = vowel
                if len(word[index:index+1]) == 1:
                    closest_vowel = vowel
                break
        if closest_vowel != "":
            break
    return closest_vowel

