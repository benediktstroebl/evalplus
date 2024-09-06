
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
    vowel_indices = [i for i, c in enumerate(word) if c in "aeiouAEIOU"]
    if vowel_indices:
        start_index = min(vowel_indices)
        end_index = max(vowel_indices)
        vowel = word[start_index:end_index+1]
        return vowel
    else:
        return ""
