
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
    start = 0
    end = len(word) - 1
    while start <= end:
        mid = (start + end) // 2
        if word[mid] == "r":
            start = mid + 1
        elif word[mid] == "t":
            end = mid - 1
        elif word[mid] == "l":
            start = mid - 1
        elif word[mid] == "n":
            end = mid + 1
        else:
            end = mid - 1
    return "" if start > end else word[start]