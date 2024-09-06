
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
    
    vowels = re.compile(r"aeiou")
    start = 0
    end = len(word) - 1
    while start < end:
        if vowels.search(word[(end - 1):(start + 1)]):
            return word[(end - 1):(start + 1)]
        else:
            start += 1
        
    return word[end]
    
get_closest_vowel("yogurt")
get_closest_vowel("FULL")
get_closest_vowel("quick")
get_closest_vowel("ab")