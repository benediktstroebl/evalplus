
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
    new_list = []
    for i in word:
        if i.isalpha():
            new_list.append(i)
    
    if len(new_list) == 0:
        return ''
    
    left = min(new_list)
    right = max(new_list)
    
    if (left == 'A' or left == 'E' or left == 'I' or left == 'O' or left == 'U') and (right == 'A' or right == 'E' or right == 'I' or right == 'O' or right == 'U'):
        return left
    else:
        return get_closest_vowel(word[:-1
