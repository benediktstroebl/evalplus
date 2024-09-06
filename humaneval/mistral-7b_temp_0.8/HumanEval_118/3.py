
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    right = []
    left = []
    for i in range(len(word)):
        if word[i].lower() in vowels:
            if i == 0 or i == len(word) - 1:
                pass
            else:
                right.append(word[i])
                left.append(word[i - 1])
    right.sort()
    left.sort()
    right.reverse()
    left.reverse()
    for i in range(len(right)):
        if right[i] == left[i]:
            return right[i]



