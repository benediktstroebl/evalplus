
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
    for i in range(len(word) - 2, -1, -1):
        for j in range(i+1, len(word)):
            if word[i] == 's' or word[i] == 'x' or word[i] == 'z' or word[i] == 'l' or word[i] == 'v' or word[i] == 'c' or word[i] == 'g' or word[i] == 'b':
                if word[j] in 'a', 'e', 'i', 'o', 'u':
                    return word[i]
    return ''
