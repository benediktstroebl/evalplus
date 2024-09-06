
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
    word = word.upper()
    length = len(word)
    vowel_index = []
    for i in range(length):
        if word[i] in "aeiouAEIOU":
            vowel_index.append(i)
    if vowel_index:
        middle_index = vowel_index[len(vowel_index)//2]
        consonant_index = middle_index + 1
        for i in range(middle_index, length):
            if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
                return word[middle_index:consonant_index]
    return ""