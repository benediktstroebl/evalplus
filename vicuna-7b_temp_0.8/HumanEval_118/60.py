
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
    first_half = word[:len(word) // 2]
    last_half = word[len(word) // 2:]
    vowel = None
    start = 0
    for i in range(len(first_half)):
        if first_half[i] == last_half[start].lower():
            start += 1
        if first_half[i] == last_half[start].upper():
            start += 1
        if first_half[i] == last_half[start].upper() and first_half[i] == last_half[start].lower():
            start += 1
        if first_half[i] == last_half[start].lower() and first_half[i] == last_half[start].upper():
            start += 1
        if first_half[i] == last_half[start].lower() and first_half[i] == last_half[start].upper() and first_half[i] == last_half[start].lower():
            start += 1
        if first_half[i] == last_half[start].upper() and first_half[i] == last_half[start].lower() and first_half[i] == last_half[start].upper():
            start += 1
    if vowel is None:
        return ""
    else:
        return vowel