
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
    vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    vowel_closest_count = float('inf')
    closest_vowel = ''

    for char in word:
        vowel_count[char] += 1

        if vowel_count['a'] <= vowel_closest_count:
            closest_vowel = char
            vowel_closest_count = vowel_count['a']
        elif vowel_count['e'] <= vowel_closest_count:
            closest_vowel = char
            vowel_closest_count = vowel_count['e']
        
    return
