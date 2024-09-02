
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

    closest_vowel = ""
    for letter_index in range(len(word)):
        if word[letter_index] in "aeiou":
            closest_vowel = word[letter_index]
            break
    for vowel in "aeiou":
        if vowel in word and word.rindex(vowel) > word.index(closest_vowel):
            closest_vowel = vowel
            break
    return closest_vowel


