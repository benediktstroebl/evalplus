
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
    word = word.strip()
    left_vowel, right_vowel = 0, 0
    
    for i in range(len(word)):
        if word[i].lower() in 'aeiou':
            left_vowel += 1
        else:
            right_vowel += 1
    
    if left_vowel <= right_vowel:
        return word[right_vowel:]
    else:
        return word[left_vowel - 1
