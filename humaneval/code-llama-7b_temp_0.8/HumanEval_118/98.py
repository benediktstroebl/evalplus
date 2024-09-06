
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
    def find_closest_vowel(word, left, right):
        if left == len(word):
            return ""
        if right == 0:
            return ""
        if right - left == 1:
            return ""
        if word[right - 2] in 'aeiou':
            return ""
        if word[right - 1] in 'aeiou':
            return word[right - 1]
        if word[right] in 'aeiou':
            return ""
        if word[left] in 'aeiou':
            return word[left]
        return find_closest_vowel(word, left + 1, right - 1)
        
    result = ""
    left = 0
    right = len(word) - 1
    while result == "":
        result = find_closest_vowel(word, left, right)
        left += 1
        right -= 1
        if left == len(word):
            return result
        if right == 0:
            return result
    return result
