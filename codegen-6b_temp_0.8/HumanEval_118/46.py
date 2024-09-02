
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
    # vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_index = 0
    for i in range(len(word) - 1, -1, -1):
        if word[i] in vowels:
            vowel_index = i
            break
    if vowel_index == 0:
        return word[0]
    if vowel_index == len(word) - 1:
        return word[-1]
    nearest_vowel = vowels[vowel_index + 1]
    bigger_vowel = word[vowel_index]
    if (ord(bigger_vowel) - ord(nearest_vowel)) % 2 == 0:
        return word[vowel_index + 1]
    else:
        return word[vowel_index - 1]
