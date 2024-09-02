
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
    word_length = len(word)
    right_half = word[word_length//2:word_length//2+2]
    consonants = word[word_length//2-2:word_length]
    for i in range(len(consonants)):
        for j in range(len(right_half)):
            if j < len(consonants) - 2:
                if word[j] in consonants[i+1:] and word[j] not in consonants[:i+1]:
                    consonants = consonants[:i+1]
                    right_half = right_half[:j] + right_half[j+1:]
                    break
    if consonants == "":
        return ""
    for vowel in vowels:
        if vowel == word[0]:
            continue
        if vowel == right_half[0]:
            continue
        if word[0] == vowel:
            continue
        if vowel == word[-1]:
            continue
        if vowel == right_half[-1]:
            continue
    return vowel
