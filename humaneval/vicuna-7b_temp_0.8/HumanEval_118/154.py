
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
    if word == '':
        return ''
    words = word.split()
    for i in range(len(words)-1):
        for j in range(i+1, len(words)):
            if words[i] == 's' or words[i] == 'l' or words[i] == 't' or words[i] == 'p' or words[i] == 'n' or words[i] == 'm' or words[i] == 'w':
                if words[j] == 'a' or words[j] == 'e' or words[j] == 'i' or words[j] == 'u' or words[j] == 'o' or words[j] == 'y':
                    closest = max(words[i].lower(), words[j].lower(), key=lambda x: len(x.lower())+abs(ord(x)-ord('a')))
                    return closest
            elif words[i] == 'v' and words[j] == 'a' or words[i] == 'v' and words[j] == 'i' or words[i] == 'v' and words[j] == 'u':
                if words[j] == 'a' or words[j] == 'e' or words[j] == 'i' or words[j] == 'u' or words[j] == 'o' or words[j] == 'y':
                    closest = max(words[i].lower(), words[j].lower(), key=lambda x: len(x.lower())+abs(ord(x)-ord('a')))
                    return closest
    return ''