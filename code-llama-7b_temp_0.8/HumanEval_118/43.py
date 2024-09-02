
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
    # find the position of the first vowel
    first_vowel_pos = -1
    for i in range(len(word)):
        if word[i].lower() in 'aeiouy':
            first_vowel_pos = i
            break

    # check if there is no vowel or the only vowel is at the beginning
    if first_vowel_pos == -1 or first_vowel_pos == 0:
        return ""
    
    # find the position of the last vowel
    last_vowel_pos = -1
    for j in range(len(word)-1, -1, -1):
        if word[j].lower() in 'aeiouy':
            last_vowel_pos = j
            break
    
    # check if there is no vowel or the only vowel is at the end
    if last_vowel_pos == -1 or last_vowel_pos == len(word)-1:
        return ""

    # find the closest vowel
    closest_vowel_pos = -1
    for i in range(first_vowel_pos, last_vowel_pos):
        if word[i].lower() in 'aeiouy':
            closest_vowel_pos = i
            break

    return word[closest_vowel_pos]


