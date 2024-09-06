
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

    closest_vowel = ''
    for index, letter in enumerate(word):
        if letter not in 'aeiouAEIOU':
            continue
        left_index = index-1
        right_index = index
        while left_index >= 0 and right_index < len(word):
            left = word[left_index]
            right = word[right_index]
            if left not in 'aeiouAEIOU':
                left_index -= 1
                continue
            elif right not in 'aeiouAEIOU':
                right_index += 1
                continue
            else:
                closest_vowel = right
                break
    return closest_vowel
