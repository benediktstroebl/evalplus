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
    # Using dictionary to do case insensitive conversion, assuming English only
    conv = str.maketrans('', '', str.ascii_lowercase)
    vowels = ['a', 'e', 'i', 'o', 'u']
    # Count number of vowels and consonants at beginning and end
    condens, vowelsets = 0, 0
    for char in word:
        if char not in vowels and char not in conv:
            condens += 1
        elif char in vowels:
            vowelsets += 1
    # Find the index of the last vowel
    last_vowel_index = len(word) - vowelsets
    # Find the closest vowel to the right of the last vowel
    dist_sum = [abs(i - last_vowel_index) for i in range(len(word))]
    closest_dist, closest_index = min(dist_sum), dist_sum.index(min(dist_sum))
    # Check that the closest vowel is between two consonants and is not an ending letter
    if closest_dist != 0 and closest_index > last_vowel_index + 1 and condens > 1:
        return word[closest_index]
    else:
        return ''