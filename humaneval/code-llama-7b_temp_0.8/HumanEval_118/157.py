
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
    vowel = 'aeiou'
    left = 0
    right = len(word)-1
    while left < right:
        if word[left] in vowel:
            if word[left] != word[left+1] and word[left+1] in vowel:
                return word[left]
            left += 1
        elif word[right] in vowel:
            if word[right] != word[right-1] and word[right-1] in vowel:
                return word[right]
            right -= 1
        elif word[left] in 'qQ' and word[left+1] in 'uU' and right == len(word)-1:
            return word[left+1]
        left += 1
        right -= 1
    return ""

