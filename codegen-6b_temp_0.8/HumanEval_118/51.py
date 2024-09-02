
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
    if len(word) == 0:
        return ""
    
    vowels = ["a", "e", "i", "o", "u"]
    word = word.lower()
    end = len(word) - 1
    start = 0
    while word[end] not in vowels:
        end -= 1
        if end == start:
            return ""
    
    end_letter = word[end]
    start_letter = word[start]

    if end_letter == start_letter:
        return start_letter
    
    mid = (end - start) / 2
    end_prev = word[end - mid - 1]
    start_next = word[start + mid]
    
    if end_prev in vowels:
        if start_next in vowels:
            return word[end - mid - 2]
        else:
            return word[end - mid - 1]
    elif start_next in vowels:
        return word[end - mid]
    else:
        return word[end - mid - 1]

