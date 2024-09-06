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
    # using find to find indices of all characters in word
    # using lambdas to create functions to check if char is a consonant or vowel
    # taking rightmost consonant's index to find closest vowel
    # checking the rightmost consonant's index to closest vowel on both sides
    # if no potential vowels are found, return an empty string
    right_consonant_index = word.rfind(lambda word: any(word.startswith(c) or word.endswith(c) for c in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"), 0, len(word) - 1) + 1
    if right_consonant_index <= 0:
        return ""
    return word[right_consonant_index].lower() if word[right_consonant_index].lower() in "aeiou" else word[right_consonant_index - 1].lower() if right_consonant_index >= 1 else word[right_consonant_index + 1].lower() if right_consonant_index < len(word) - 1 else ""