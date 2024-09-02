
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
    assert type(word) == str

    vowels = ["A", "E", "I", "O", "U"]
    vowels_indices = []

    for i, char in enumerate(word[::-1]):
        if char in vowels:
            vowels_indices.append(i)
            break

    if len(vowels_indices) == 0:
        return ""

    # find the first vowel from right side
    vowel_idx = vowels_indices[0]
    right_vowels = []
    for i in range(vowel_idx, len(word)):
        if word[i] in vowels:
            right_vowels.append(word[i])
    if len(right_vowels) == 0:
        return ""

    # find the first vowel from left side
    vowel_idx = vowels_indices[-1]
    left_vowels = []
    for i in range(vowel_idx, -1, -1):
        if word[i] in vowels:
            left_vowels.append(word[i])
    if len(left_vowels) == 0:
        return ""

    if right_vowels[0] == left_vowels[-1]:
        return right_vowels[0]
    else:
        return left_vowels[-1]

