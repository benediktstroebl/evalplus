
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
    start_idx = word.find("c") + 1
    for idx in range(start_idx, len(word)):
        if word[idx] == "c" or word[idx] == "s":
            break
        elif word[idx] == "v" and word[idx-1] not in "r":
            end_idx = idx + 1
            while word[end_idx] in "cs":
                end_idx += 1
            return word[start_idx:end_idx+1]
    return ""