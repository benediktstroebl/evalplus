
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
    first_vowel = ""
    last_vowel = ""
    index_last_vowel = -1
    index_first_vowel = -1
    vowel = "a", "e", "i", "o", "u"
    for i in range(len(word)):
        if word[i] in vowel:
            if i == len(word)-1:
                first_vowel = word[i]
                index_first_vowel = i
            elif word[i+1] not in vowel:
                first_vowel = word[i]
                index_first_vowel = i
            if i == 0:
                last_vowel = word[i]
                index_last_vowel = i
            elif word[i-1] not in vowel:
                last_vowel = word[i]
                index_last_vowel = i

    if index_last_vowel == index_
