
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
    for i in range(len(word)-1, -1, -1):
        for j in range(i+1, len(word)):
            if word[i] == 'r' and word[j] == 'n' or word[i] == 't' and word[j] == 's':
                continue
            if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u' and word[j] == 'b' or word[j] == 'd' or word[j] == 'f' or word[j] == 'g' or word[j] == 'h' or word[j] == 'p' or word[j] == 'v' or word[j] == 'z':
                return word[i]
    return ''