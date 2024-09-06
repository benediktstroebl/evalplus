def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that 
    stands between two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending don't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    # using regex to check right-aligned vowels
    import re
    
    matches = re.findall(r'(?<!^)(?<!\w\w)\b\w{1,2}\b(?=\w\w)(?=\w)', word)
    if matches: 
        return matches[0]
    else: 
        return ""