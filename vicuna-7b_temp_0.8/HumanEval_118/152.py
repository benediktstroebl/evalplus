
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
    vowels = "aeiou"
    if len(word) < 2 or len(word) > 2:
        return ""
    if word[0] in vowels:
        return word[0]
    first_char = word[1]
    for i in range(len(vowels)):
        index = word.find(vowels[i])
        if index == -1:
            continue
        for j in range(i+1, len(vowels)):
            index2 = word.find(vowels[j])
            if index2 == -1:
                continue
            if index < index2:
                return vowels[i]
    return ""