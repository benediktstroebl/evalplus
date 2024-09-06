
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

    if not word:
        return ""

    start = 0
    end = len(word) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if word[mid] == "a" or word[mid] == "e" or word[mid] == "i" or word[mid] == "o" or word[mid] == "u":
            return word[mid]
        elif word[mid] == "y":
            start = mid + 1
        else:
            end = mid - 1

    if start > 0:
        return word[start - 1]
    else:
        return ""

