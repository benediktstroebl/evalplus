
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
    chars = [x for x in word]

    max_index = len(chars) - 1
    for i in range(len(chars) - 1, -1, -1):
        char = chars[i]
        # If the char is a vowel
        if char in 'aeiou':
            max_index = i
            break

    min_index = len(chars)
    for i in range(len(chars) - 1, -1, -1):
        char = chars[i]
        if char in 'aeiou':
            min_index = i
            break

    if min_index > max_index:
        return ''

    left_to_right = chars[:min_index]
    right_to_left = chars[max_index:]

    for i in range(1, len(left_to_right)):
        curr = left_to_right[-i]
        prev = left_to_right[-i-1]
        # If the prev and current are not the same in both directions
        if prev != curr:
            if char == 'u':
                return curr
            else:
                return prev

    return chars[0]

