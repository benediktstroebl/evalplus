
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
    # your code here
    # (0) make empty list
    # (1) for each letter in word
    # (2) if letter is vowel
    #     (a) loop through list
    #     (b) if next letter is consonant
    #         (i) insert vowel into list at next index
    # (3) return first item in list

    # (1)
    letters = []
    # (2)
    for letter in word:
        # (3)
        if letter in 'aeiou':
            # (4)
            for i in range(len(letters)):
                # (5)
                if letters[i] in 'bcdfghjklmnpqrstvwxyz':
                    # (6)
                    letters.insert(i+1, letter)
                    # (7)
                    break

    # (8)
    return letters[0] if letters else ''
