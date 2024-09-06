
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
    n = len(word)
    start = 0
    closest_distance = float('inf')
    closest_vowel = ''
    for i in range(1, n):
        # print("i is",i)
        if word[i] in 'bcdfghjklmnpqrstvwxyz':
            if i == 0:
                # check distance between first consonant and closest vowel
                if abs(start - n-1) < closest_distance:
                    closest_distance = abs(start - n-1)
                    closest_vowel = word[start]
                    start = i
            elif i == n-1:
                # check distance between last consonant and closest vowel
                if abs(i-1) < closest_distance:
                    closest_distance = abs(i-1)
                    closest_vowel = word[i-1]
                    start = i
        elif word[i] in 'aeiou':
            if i - start == 1:
                # check distance between vowel and closest consonant
                if abs(i - closest_distance) < closest_distance:
                    closest_distance = abs(i - closest_distance)
                    closest_vowel = word[i]
                    start = i
            elif i - start == 2:
                # check distance between vowel and closest consonant
                if abs(i - closest_distance) < closest_distance:
                    closest_distance = abs(i - closest_distance)
                    closest_vowel = word[i]
                    start = i
            elif i - start == 3:
                # check distance between vowel and closest consonant
                if abs(i - closest_distance) < closest_distance:
                    closest_distance = abs(i - closest_distance)
                    closest_vowel = word[i]
                    start = i
    if closest_vowel == '':
        return ''
    else:
        return closest_vowel