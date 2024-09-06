
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
    vowel = ""
    i = len(word) - 1
    for j in range(len(word) - 2, -1, -1):
        if word[j] == word[j+1] and word[j] in "aeiouAEIOU":
            distance = 1
            while j > i and word[j] == word[j-1] and word[j] in "aeiouAEIOU":
                distance += 1
                j -= 1
            if distance == 2:
                vowel = word[i]
                break
        elif word[j] == "r" and word[j+1] == "t":
            break
        i -= 1
    return vowel
