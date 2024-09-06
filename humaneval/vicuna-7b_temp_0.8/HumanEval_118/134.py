
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
    for i in range(len(word)-1):
        for j in range(i+1, len(word)):
            if not (word[i] in "bcdfghjklmnpqrstvwxz" or word[j] in "bcdfghjklmnpqrstvwxz"):
                if word[i] == word[j] and (word[i+1] in "aeiou" or word[i-1] in "aeiou"):
                    return word[i]
    return ""
