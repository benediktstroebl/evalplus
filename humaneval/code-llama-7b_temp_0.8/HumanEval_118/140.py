
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
    # My solution
    # 1. find the index of the right most consonant
    # 2. find the index of the left most vowel, by using list slicing
    # 3. find the vowels between them
    def find_vowels(word):
        vowels = []
        for ch in word:
            if ch in ['a', 'e', 'i', 'o', 'u']:
                vowels.append(ch)
        return vowels

    def find_index(word):
        # assume that the word has at least one consonant
        index = len(word) - 1
        while index >= 0:
            if word[index] in ['a', 'e', 'i', 'o', 'u']:
                break
            index -= 1
        return index
    
    index = find_index(word)
    vowels = find_vowels(word)

    if index == 0:
        return ""
    left_vowels = find_vowels(word[:index])
    if left_vowels:
        return left_vowels[-1]
    else:
        return ""

    # My solution 2
    def find_vowels(word):
        vowels = []
        for i, ch in enumerate(word):
            if ch in ['a', 'e', 'i', 'o', 'u']:
                vowels.append((i, ch))
        return vowels

    vowels = find_vowels(word)

    if len(vowels) == 0:
        return ""
    elif len(vowels) == 1:
        return vowels[0][1]
    else:
        right_index = vowels[-1][0]
        for i, ch in enumerate(word[::-1]):
            if ch in ['a', 'e', 'i', 'o', 'u']:
                return ch
            elif i > right_index:
                break
    return ""


    # My solution 3
    index = len(word) - 1
    
