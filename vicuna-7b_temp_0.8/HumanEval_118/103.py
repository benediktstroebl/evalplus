
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
    vowel_index = [i for i, c in enumerate(word) if c in "aeiouAEIOU"]
    if vowel_index:
        start_index = vowel_index[-1]
        for i in range(start_index-1, -1, -1):
            if word[i] in "bcdfghjklmnpqrstvwxyz":
                break
        end_index = word.index(word[i], start_index) + 1
        return word[start_index:end_index]
    else:
        return ""
