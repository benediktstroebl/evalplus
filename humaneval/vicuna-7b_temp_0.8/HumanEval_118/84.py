
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
    words = word.split()
    start = 0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[i] == 's' or words[i] == 't' or words[i] == 'p' or words[i] == 'h' or words[i] == 'w':
                continue
            if words[j] == 'a' or words[j] == 'e' or words[j] == 'i' or words[j] == 'o' or words[j] == 'u':
                break
            if words[i] == words[j]:
                continue
            if words[i] == 'r' and words[j] == 'n':
                break
            if words[i] == 'm' and words[j] == 'b':
                break
    if i == 0 or i == len(words) - 1 or j == 0 or j == len(words) - 1:
        return ""
    return words[i]