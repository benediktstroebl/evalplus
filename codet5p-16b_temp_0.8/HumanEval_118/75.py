
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

    positions = []
    for i, l in enumerate(word):
        if l not in "aeiou":
            continue
        if i + 1 < len(word) and word[i + 1] not in "aeiou":
            positions.append(i)
    if not positions:
        return ""
    min_distance = positions[-1] - positions[0]
    positions.sort()
    positions.append(positions[-1] + min_distance)
    for i in range(len(positions) - 1):
        if positions[i + 1] - positions[i] < min_distance:
            min_distance = positions[i + 1] - positions[i]
            result = word[positions[i] + 1:positions[i + 1]]
    return result

