
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
    words = word.split(' ')
    vowels = set(('a', 'e', 'i', 'o', 'u'))
    vowel_position = set()

    for word in words:
        if word.lower() == 'a':
            vowel_position.add(0)
        elif word.lower() == 'e':
            vowel_position.add(1)
        elif word.lower() == 'i':
            vowel_position.add(2)
        elif word.lower() == 'o':
            vowel_position.add(3)
        elif word.lower() == 'u':
            vowel_position.add(4)

    for i in range(len(words)):
        if words[i].lower() == 'a':
            vowel_position.remove(0)
        elif words[i].lower() == 'e':
            vowel_position.remove(1)
        elif words[i].lower() == 'i':
            vowel_position.remove(2)
        elif words[i].lower() == 'o':
            vowel_position.remove(3)
        elif words[i].lower() == 'u':
            vowel_position.remove(4)

    closest_vowel = None
    closest_distance = float('inf')

    for vowel in vowels:
        vowel_index = vowel_position.index(vowel)
        distance = abs(vowel_index - words[0].lower().index(vowel))
        if distance < closest_distance:
            closest_distance = distance
            closest_vowel = vowel

    return closest_vowel.lower() if closest_vowel else ''
