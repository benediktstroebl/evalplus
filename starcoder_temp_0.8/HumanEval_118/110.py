
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        if vowel in word:
            vowel_index = word.index(vowel)
            if vowel_index > 0 and vowel_index < len(word) - 1:
                right_consonant = word[vowel_index + 1]
                left_consonant = word[vowel_index - 1]
                if right_consonant.lower() not in vowels and left_consonant.lower() not in vowels:
                    return vowel
    return ''
