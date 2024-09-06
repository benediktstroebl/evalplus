
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
    vowel_count = 0
    for index, vowel in enumerate(word):
        if index == 0 or index == len(word) - 1:
            continue
        elif vowel in "aeiouAEIOU":
            vowel_count += 1
        else:
            return ""
    if vowel_count == 0:
        return ""
    if vowel_count % 2 == 0:
        return word[-vowel_count + 1:-1]
    return word[-vowel_count:
