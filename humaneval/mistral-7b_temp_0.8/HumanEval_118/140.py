
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

    vowels = ["a", "e", "i", "o", "u"]
    vowel_list = []

    for i in range(0, len(word)):
        if word[i] in vowels:
            vowel_list.append(i)

    if len(vowel_list) == 0:
        return ""
    elif len(vowel_list) == 1:
        return word[vowel_list[0]]
    else:
        middle_vowel_index = vowel_list[1]
        return word[middle_vowel_index]

