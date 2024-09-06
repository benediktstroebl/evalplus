
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
    result = ""

    # find the position of vowel
    for i in range(len(word) - 1, -1, -1):
        if word[i].lower() in "aeiou":
            break
    
    if i == len(word) - 1:
        return result

    vowel_pos = i

    # find the position of consonant
    for j in range(len(word) - 1, i, -1):
        if word[j].lower() not in "aeiou":
            break
    
    consonant_pos = j

    # find the position of closest vowel
    for k in range(j - 1, i, -1):
        if word[k].lower() in "aeiou":
            if abs(k - vowel_pos) < abs(consonant_pos - vowel_pos):
                result = word[k]
            else:
                result = word[consonant_pos]
            break

    return result
