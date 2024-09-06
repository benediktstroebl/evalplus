
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
    if len(word) < 2:
        return ""

    for i in range(len(word)-1, 0, -1):
        for j in range(i+1, len(word)):
            if word[i] == "b" or word[i] == "d" or word[i] == "f" or word[i] == "h" or word[i] == "k" or word[i] == "m" or word[i] == "n" or word[i] == "p" or word[i] == "r" or word[i] == "s" or word[i] == "t" or word[i] == "w" or word[i] == "y":
                continue
            elif word[i] == "c" and word[j] == "a":
                if word[i+1] == "t":
                    if word[j+1] == "i":
                        return "i"
                    elif word[j+1] == "e":
                        return "e"
            elif word[i] == "s" and word[j] == "a":
                if word[i+1] == "t":
                    if word[j+1] == "i":
                        return "i"
                    elif word[j+1] == "e":
                        return "e"
            elif word[i] == "h" and word[j] == "a":
                if word[i+1] == "u":
                    if word[j+1] == "o":
                        return "o"
            elif word[i] == "t" and word[j] == "a":
                if word[i+1] == "r":
                    if word[j+1] == "i":
                        return "i"
                    elif word[j+1] == "e":
                        return "e"
    return ""
