
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
    if len(word) < 2:
        return ""
    left_idx = len(word) - 1
    right_idx = 0
    min_dist = float('inf')
    for idx in range(len(word) - 1):
        if word[idx] in "bcdfghjklmnpqrstvwxyz":
            dist = (idx + 1 - right_idx) * 10000
            if dist < min_dist:
                min_dist = dist
            if word[idx] == word[right_idx] or word[idx] == "e" or word[idx] == "i" or word[idx] == "o" or word[idx] == "u":
                right_idx += 1
        else:
            right_idx += 1
    return word[left_idx:right_idx + 1]
