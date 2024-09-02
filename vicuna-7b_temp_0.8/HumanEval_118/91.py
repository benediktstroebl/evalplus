
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
    start = 0
    end = 0
    closest = ""
    for i in range(len(word)-1):
        if word[i:i+2] == "cc":
            start = i+1
            end = start
        elif word[i:i+2] == "tt":
            start = i+1
            end = start
        elif word[i:i+2] == "nk":
            start = i+1
            end = start
        elif word[i:i+2] == "pq":
            start = i+2
            end = start
        elif word[i:i+2] == "rj":
            start = i+1
            end = start
            for j in range(end, len(word)):
                if word[j] == "a":
                    closest = word[start:j]
                    break
                elif word[j] == "e":
                    closest = word[start:j]
                    break
                elif word[j] == "i":
                    closest = word[start:j]
                    break
                elif word[j] == "o":
                    closest = word[start:j]
                    break
                elif word[j] == "u":
                    closest = word[start:j]
                    break
                elif word[j] == "y":
                    closest = word[start:j]
                    break
                elif word[j] == "y":
                    closest = word[start:j]
                    break
    return closest
