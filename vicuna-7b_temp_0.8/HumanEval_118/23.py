
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
    # convert the word to lowercase
    word = word.lower()
    # split the word by whitespace
    words = word.split()
    # initialize variables for the previous and next consonants
    prev_cons = ''
    next_cons = ''
    # iterate through the words
    for i in range(len(words)):
        # get the previous and next cons
        prev_cons = words[i - 1]
        next_cons = words[i]
        # get the index of the consonant
        con_idx = next_cons.index('c') + 1
        # get the index of the consonant in the previous word
        prev_con_idx = prev_cons.index('c') + 1
        # if the current consonant is the rightmost one
        if i == len(words) - 1:
            # get the index of the vowel
            vowel_idx = next_cons.index('a') + 1
        else:
            # get the index of the vowel
            vowel_idx = next_cons.index('a') + 1
        # if the vowel is not empty
        if vowel_idx != -1:
            # get the distance between the current consonant and the vowel
            distance = abs(con_idx - vowel_idx)
            # if the distance is less than the previous distance
            if distance < previous_distance:
                # update the previous consonant and previous distance
                prev_cons = next_cons
                previous_distance = distance
        # if the current consonant is the rightmost one
        if i == len(words) - 1:
            # update the next consonant
            next_cons = 'a' + next_cons
        # update the previous consonant
        prev_cons = next_cons
    # return the closest vowel
    return prev_cons