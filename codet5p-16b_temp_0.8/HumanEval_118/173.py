
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

    for i in reversed(range(len(word))):
        if word[i] == 'a' or word[i] == 'e' or word[i] == 'o' or word[i] == 'u' or word[i] == 'A' or word[i] == 'E' or word[i] == 'O' or word[i] == 'U':
            return word[i]
        if word[i] == 'b' or word[i] == 'c' or word[i] == 'd' or word[i] == 'f' or word[i] == 'g' or word[i] == 'h' or word[i] == 'j' or word[i] == 'k' or word[i] == 'l' or word[i] =='m' or word[i] == 'n' or word[i] == 'p' or word[i] == 'q' or word[i] == 'r' or word[i] =='s' or word[i] == 't' or word[i] == 'v' or word[i] == '
