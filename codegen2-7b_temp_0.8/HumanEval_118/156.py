
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
    
    letters = [char.upper() for char in word]
    begin_idx = 0
    end_idx = len(letters)-1
    
    while begin_idx < end_idx:
        vowel = letters[begin_idx] + letters[end_idx]
        if vowel.startswith('AEIOU'):
            begin_idx += 1
        else:
            begin_idx += 1
            end_idx -= 1
            
    if begin_idx >= end_idx:
        return ""
    else:
        return letters[begin_idx] + letters[end_id
