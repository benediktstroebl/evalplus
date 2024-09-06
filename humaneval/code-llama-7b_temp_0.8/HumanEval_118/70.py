
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

    # R1 - find the position of the right most vowel
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    vowels_list = []
    for c in word:
        if c in vowels:
            vowels_list.append(word.index(c))
    # print(vowels_list)
    if len(vowels_list) == 0:
        return ""
    right_most_vowel = max(vowels_list)
    
    # R2 - find the position of the right most consonant
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    consonants_list = []
    for c in word:
        if c in consonants:
            consonants_list.append(word.index(c))
    # print(consonants_list)
    if len(consonants_list) == 0:
        return ""
    right_most_consonant = max(consonants_list)

    # R3 - find the closest vowel between the right most consonant and vowel
    if right_most_consonant < right_most_vowel:
        left_to_vowel = word[right_most_consonant + 1 : right_most_vowel]
        if len(left_to_vowel) == 0:
            return ""
        else:
            for c in left_to_vowel:
                if c in vowels:
                    return c
    else:
        right_to_vowel = word[
