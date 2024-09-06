
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

    vowels = "AEIOU"
    left = 0
    right = len(word)-1
    closest_vowel = ""
    while left < right:
        left_ch = word[left]
        right_ch = word[right]
        if left_ch not in vowels and right_ch not in vowels:
            left += 1
            right -= 1
            continue
        if left_ch in vowels and right_ch in vowels:
            continue
        elif left_ch in vowels and right_ch not in vowels:
            closest_vowel = word[left]
            left += 1
            continue
        elif left_ch not in vowels and right_ch in vowels:
            closest_vowel = word[right]
            right -= 1
            continue
        else:
            left_vowel = word[left]
            right_vowel = word[right]
            left_d = vowels.find(left_vowel)
            right_d = vowels.find(right_vow
