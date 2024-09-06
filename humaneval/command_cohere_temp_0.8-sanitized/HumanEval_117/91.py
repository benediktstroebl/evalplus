def select_words(s, n):
    """
    Given a string s and a natural number n, returns a list of all words from string s that contain exactly n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    """
    # dictionary to count number of consonants in each word
    word_counts = {}
    
    # iterate through the string to count number of consonants
    for word in s.split():
        # remove spaces from the word
        word = word.replace(' ', '')
        # check if the word is empty
        if word == "":
            continue
        # count consonants using the vowels dictionary
        consonant_count = len([char for char in word if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"])
        word_counts[word] = consonant_count
    
    # return all words with exactly n consonants
    return [word for word, count in word_counts.items() if count == n]