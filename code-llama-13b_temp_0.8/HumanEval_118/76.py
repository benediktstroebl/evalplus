
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
    vowels = "aeiouAEIOU"
    vowel_positions = []
    for i,char in enumerate(word):
        if char in vowels:
            vowel_positions.append(i)
    vowel_pairs = zip(vowel_positions, vowel_positions[1:])
    shortest_dist = 1e5
    closest_vowel = ""
    for pair in vowel_pairs:
        if pair[0] > 0 and pair[1] < len(word)-1 and (pair[1] - pair[0]) < shortest_dist:
            shortest_dist = pair[1] - pair[0]
            closest_vowel = word[pair[0]]
    return closest_vowel

