
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    # check if there is a space in the string
    if ' ' not in s:
        return []

    # strip the string and split into an array of words
    s_clean = s.strip().split(' ')

    # init output list
    out = []

    # iterate words
    for word in s_clean:
        # remove white space
        word_clean = word.strip()

        # if the length of the word is greater or equal to the number of consonants
        if len(word_clean) >= n:
            # init counters
            v_counter = 0
            c_counter = 0

            # iterate characters
            for c in word_clean:
                # if the character is a vowel
                if c in ['a', 'e', 'i', 'o', 'u']:
                    # increment vowel counter
                    v_counter += 1
                # else
                else:
                    # increment consonant counter
                    c_counter += 1

            # if the number of consonants equals the desired n
            if c_counter == n:
                # append to output
                out.append(word_clean)

    # return the output list
    return out

