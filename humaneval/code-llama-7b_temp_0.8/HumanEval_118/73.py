
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

    # check if the word has no vowels
    # if so, return empty string
    if "A" not in word and "E" not in word and "I" not in word and "O" not in word and "U" not in word:
        return ""

    # save the last vowel's index
    last_vowel_idx = len(word)

    # save the first non-vowel's index
    first_non_vowel_idx = len(word)

    # count the number of vowels in the word
    # if the count is 0 or 1, return empty string
    num_of_vowels = 0
    for char in word:
        if char in "AEIOU":
            num_of_vowels += 1
            if num_of_vowels == 2:
                break

    if num_of_vowels <= 1:
        return ""

    # save the last non-vowel's index
    last_non_vowel_idx = len(word)

    # loop through the word from the back
    for i, char in enumerate(word[::-1]):

        # save the first vowel's index
        if char in "AEIOU":
            last_vowel_idx = i
            break
        else:
            last_non_vowel_idx = i

    # if the last vowel's index is before the last non-vowel's index
    # return the first non-vowel's index
    if last_vowel_idx < last_non_vowel_idx:
        return word[last_non_vowel_idx]

    # else return the last vowel's index
    return word[last_vowel_idx]

