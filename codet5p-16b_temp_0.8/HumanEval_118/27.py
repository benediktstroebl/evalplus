
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

    
    closest_vowel = ""

    if not word:
        return ""

    for i, ltr in enumerate(word):
        if ltr not in "aeiou" or i == 0 or i == len(word) - 1:
            continue

        for j in range(i+1, len(word)):
            if word[j] not in "aeiou":
                closest_vowel = word[j]
                break

            if word[j] == "a" or word[j] == "e" or word[j] == "i" or word[j] == "o" or word[j] == "u":
                closest_vowel = word[j]
                break

        break

    return closest_vowel
