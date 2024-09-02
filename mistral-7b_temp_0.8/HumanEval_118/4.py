
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
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    vowel_index = -1

    for i, char in enumerate(word):
        if char in vowels and vowel_index == -1:
            vowel_index = i

        if i > vowel_index and char not in vowels:
            result = word[vowel_index + 1]
            break

    return result


































































































































