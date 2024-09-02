
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
    word = word.lower()
    if len(word) < 2:
        return ""
    left, middle, right = 0, 1, len(word)
    for i in range(1, len(word)):
        if word[i] == word[i-1] and word[i] in "aeiou":
            vowel_index = word.index(word[i]) + 1
        else:
            vowel_index = 0
        if middle > 0 and word[middle-1] == word[middle-2] and word[middle-1] in "aeiou":
            previous_vowel = word[middle-2]
            next_vowel = word[middle-1]
        else:
            previous_vowel = None
            next_vowel = word[middle-1]
        if word[left] == word[right] and word[left] in "aeiou" and \
           previous_vowel not in "aeiou" and next_vowel not in "aeiou" and \
           (vowel_index - 1) * 2 > (previous_vowel - 1) * 2 and \
           (vowel_index - 1) * 2 < (next_vowel - 1) * 2:
            return word[left]
        if middle > 0 and word[middle-1] == word[middle-2] and word[middle-1] in "aeiou":
            previous_vowel = word[middle-2]
            next_vowel = word[middle-1]
        left = i
        middle = max(middle-1, 0)
    return ""
