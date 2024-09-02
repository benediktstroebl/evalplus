
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
    vowels = "aeiouAEIOU"
    vowel_indices = [i for i, char in enumerate(word) if char in vowels]
    if not vowel_indices:
        return ""
    first_vowel_index = vowel_indices[0]
    next_consonant_index = word.find(vowel_indices[0], first_vowel_index + 1)
    if next_consonant_index == -1:
        return ""
    second_vowel_index = vowel_indices[1]
    if first_vowel_index == second_vowel_index:
        return ""
    distance = abs(first_vowel_index - second_vowel_index)
    return word[second_vowel_index + 1:next_consonant_index]
