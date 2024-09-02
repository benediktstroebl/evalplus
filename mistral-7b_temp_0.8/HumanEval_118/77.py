
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
    word = list(word)
    left, right = 0, len(word)-1
    while left < right:
        if word[left] != word[right]:
            break
        left += 1
        right -= 1
    left += 1
    right -= 1
    # print(left, right)
    if left >= right:
        return ''

    vowels = 'aeiouAEIOU'
    closest = vowels[0]
    for i in range(left, right+1):
        if word[i] in vowels:
            if vowels.index(word[i]) < vowels.index(closest):
                closest = word[i]
            break
    return closest

