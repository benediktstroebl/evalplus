
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
    vowels = 'aeiou'
    vowel_distance = len(word)
    for i in word[::-1]:
        if i in vowels:
            vowel_distance -= 1
        else:
            break
    if vowel_distance == len(word):
        return word
    vowel = word[vowel_distance]
    closest_vowel = word[vowel_distance + 1]
    for i in word[vowel_distance + 2:]:
        if i in vowels:
            continue
        else:
            closest_vowel = i
            break
    return closest_vowel

