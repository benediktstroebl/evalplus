
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
    vowels = "aeiouAEIOU"
    left = 0
    right = len(word) - 1
    while right >= left:
        mid = (left + right) // 2
        if word[mid] == word[right] and word[mid] in vowels:
            return word[mid]
        elif word[mid] in vowels:
            if len(word[mid-1]) > 0 and word[mid-1] in vowels:
                return word[mid]
        left = mid + 1
        right = len(word) - 1
    return ""