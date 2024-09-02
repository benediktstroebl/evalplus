
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
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    
    word = word.strip().lower()
    vowel_index = word.rfind('a')
    
    if vowel_index == -1:
        return ''
    
    for vowel in vowels:
        if vowel_index >= len(word)-1:
            return vowel
        
        if word[vowel_index+1].lower() in vowels:
            return vowel
    
    return ''
