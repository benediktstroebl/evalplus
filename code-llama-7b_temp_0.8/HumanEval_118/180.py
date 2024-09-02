
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
    # 1st solution: O(n) time | O(1) space
    vowels = "aeiou"
    left, right = 0, len(word) - 1
    while right > left:
        if word[left] not in vowels or word[right] not in vowels:
            left += 1
            right -= 1
            continue
        for i in range(left, right):
            if word[i] in vowels:
                return word[i]
    return ""

    # 2nd solution: O(n) time | O(1) space
    vowels = "aeiou"
    left, right = 0, len(word) - 1
    while right > left:
        if word[left] not in vowels or word[right] not in vowels:
            left += 1
            right -= 1
            continue
        for i in range(left, right):
            if word[i] in vowels:
                return word[i]
    return ""

    # 3rd solution: O(n) time | O(1) space
    vowels = "aeiou"
    left, right = 0, len(word) - 1
    while right > left:
        if word[left] not in vowels or word[right] not in vowels:
            left += 1
            right -= 1
            continue
        while right > left:
            if word[right] in vowels:
                return word[right]
            right -= 1
    return ""

    # 4th solution: O(n) time | O(1) space
    vowels = "aeiou"
    left, right = 0, len(word) - 1
    while right > left:
        if word[left] not in vowels or word[right] not in vowels:
            left += 1
            right -= 1
            continue
        while right > left:
            if word[right] in vowels:
                return word[right]
            right -= 1
    return ""

    # 5
