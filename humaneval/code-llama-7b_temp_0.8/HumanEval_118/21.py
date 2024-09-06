
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
    vowel_letters = ["a", "e", "i", "o", "u"]
    vowels = []
    for index, letter in enumerate(word):
        if letter in vowel_letters:
            if index == 0 or index == len(word)-1:
                continue
            if letter != word[index-1] and letter != word[index+1]:
                vowels.append(letter)
    if len(vowels) == 0:
        return ""
    return sorted(vowels)[0]

