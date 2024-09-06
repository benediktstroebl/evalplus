
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
    # Your code here
    words = s.split(" ")
    consonants = list('bcdfghjklmnpqrstvwxyz')
    list_of_consonants = []
    for word in words:
        consonants_in_word = []
        for letter in word:
            if letter in consonants:
                consonants_in_word.append(letter)
        list_of_consonants.append(consonants_in_word)
    consonant_count = []
    for consonant in list_of_consonants:
        consonant_count.append(len(consonant))
    n_consonants = []
    for count in consonant_count:
        if count == n:
            n_consonants.append(count)
    new_list_of_consonants = []
    for n in n_consonants:
        new_list_of_consonants.append(list_of_consonants[n])
    result = []
    for word in new_list_of_consonants:
        result.append(word)
    return result
