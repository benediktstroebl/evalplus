
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
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    def get_index(s, ch):
        try:
            return s.rindex(ch)
        except ValueError:
            return -1
    
    # A possible solution:
    # 1. find the last vowel from the right
    # 2. find the last consonant from the right
    # 3. find the first consonant from the left
    # 4. find the first vowel from the left
    # 5. find the closest between the two vowels
    last_vowel_pos = get_index(word, vowels)
    last_consonant_pos = get_index(word[::-1], consonants)
    if last_vowel_pos < 0 or last_consonant_pos < 0:
        return ""
    first_consonant_pos = get_index(word, consonants)
    first_vowel_pos = get_index(word[::-1], vowels)
    if first_consonant_pos < 0 or first_vowel_pos < 0:
        return ""
    left_vowel_pos = first_vowel_pos + 1
    if left_vowel_pos > last_vowel_pos:
        return ""
    right_vowel_pos = last_vowel_pos - 1
    if right_vowel_pos < first_vowel_pos:
        return ""
    return word[right_vowel_pos] if abs(left_vowel_pos - right_vowel_pos) < abs(first_consonant_pos - last_consonant_pos) else word[left_vowel_pos]
    
