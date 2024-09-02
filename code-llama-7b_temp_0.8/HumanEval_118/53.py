
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
    vowels_plus_space = "aeiou "
    word = word.lower()
    # vowels_plus_space = vowels + " "
    vowels_list = list(vowels_plus_space)
    index = 0
    for letter in word[::-1]:
        if letter in vowels:
            if index != 0:
                index_letter = word[len(word)-index]
                index_letter_left = word[len(word)-index+1]
                if index_letter_left in vowels_list and index_letter_left != index_letter:
                    return index_letter_left
            else:
                return index_letter
        index += 1
    return ""

