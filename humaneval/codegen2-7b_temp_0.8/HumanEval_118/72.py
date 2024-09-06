
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
    low, high = 0, len(word)-1
    while low < high:
        mid = (low + high) // 2
        if word[mid-1]!= 'a' and word[mid-1]!= 'e' and word[mid-1]!= 'i' and word[mid-1]!= 'o' and word[mid-1]!= 'u':
            low = mid + 1
        else:
            high = mid
    if low == high:
        return ''
    return word[low
