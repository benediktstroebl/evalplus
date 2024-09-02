
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
    for i in range(len(words)-1):
        for j in range(i+1, len(words)):
            if words[i] == 's' or words[i] == 'b' or words[i] == 'd' or words[i] == 'p' or words[i] == 't' or words[i] == 'h':
                if words[j] == 'a' or words[j] == 'e' or words[j] == 'i' or words[j] == 'o' or words[j] == 'u':
                    return words[i]
            elif words[i] == 'r' or words[i] == 'm' or words[i] == 'n' or words[i] == 'l':
                if words[j] == 'a' or words[j] == 'e' or words[j] == 'i' or words[j] == 'o' or words[j] == 'u':
                    return words[i]
    
    return ""
