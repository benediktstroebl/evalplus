
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
    vowels = "aeiouAEIOU"
    vowels = list(vowels)
    vowel_diffs = {vowels[i]: vowels[i + 1] for i in range(len(vowels) - 1)}
    for i in range(len(word) - 1, -1, -1):
        if word[i] not in vowels:
            continue
        vowel = word[i]
        left_char = word[:i]
        if not left_char.isalpha():
            continue
        if left_char.lower() in vowel_diffs:
            return vowel_diffs[left_char.lower()]
    return ""

