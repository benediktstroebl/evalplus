
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
    vowels = "aeiou"
    vowels_set = set(vowels)
    
    vowels_counter = { vowel: 0 for vowel in vowels }
    consonants = ""
    word = word.lower()
    
    for char in word:
        if char in vowels_set:
            vowels_counter[char] += 1
        else:
            consonants += char
            
    last_vowel_pos = len(word) - vowels_counter[vowels[0]]
    
    for i in range(last_vowel_pos + 1, len(word)):
        if word[i] in vowels_set:
            return word[i]
    
    return ""
