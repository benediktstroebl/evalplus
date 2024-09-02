
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
    first_half = word[:len(word)//2+1]
    second_half = word[len(word)//2+1:]
    vowel_index = first_half.index(get_most_frequent_vowel())
    if vowel_index != -1:
        return first_half[vowel_index]
    vowel_index = second_half.index(get_most_frequent_vowel())
    if vowel_index != -1:
        return second_half[vowel_index]
    return ""
