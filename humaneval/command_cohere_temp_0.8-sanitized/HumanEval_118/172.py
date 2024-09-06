def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that 
    stands between two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending don't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    # use a dictionary to check if current char is consonant and count recurrent consonant
    cnt = 0
    conn = {}
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    for c in word:
        if c in vowels:
            if cnt > 0:
                if c in conn:
                    conn[c] += 1
                else:
                    conn[c] = 2
        else: 
            cnt += 1
    # search the last vowel and count recurrent consonants before it
    last_vowel = 0
    for i,c in enumerate(reversed(word)):
        if c in vowels:
            if cnt > 0:
                if c in conn:
                    if conn[c] == 1:
                        last_vowel = i
                    conn[c] -= 1
            else:
                last_vowel = i
            cnt = 0
        else:
            cnt += 1
    # search for the closest vowel
    closeness = 10
    idx = -1
    for c in conn:
        if conn[c] == 1 and closeness > 1:
            closeness = 1
            idx = c
    if idx != -1:
        return word[last_vowel:idx+1].upper()
    else:
        return ""