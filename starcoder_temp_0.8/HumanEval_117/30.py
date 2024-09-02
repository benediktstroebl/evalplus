
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
    
    # In order to keep the original order of the words in the string s, 
    # we will use a list of the form: [sorted_word, original_index_of_word_in_s].
    # In the end, we will sort this list according to the original index 
    # of the words and return the words in the list.

    words = []
    for i in range(len(s)):
        if i == 0 or s[i-1] =='':
            for j in range(i+1, len(s)):
                if s[j] =='':
                    words.append([s[i:j], i])
                    break
                
    # Create a set of words from the words list.
    # Each word in the set is of the form: (consonants, original_index_of_word_in_s)
    words_set = set()
    for i in range(len(words)):
        consonants = 0
        for j in range(len(words[i][0])):
            if words[i][0][j] not in 'aeiou':
                consonants += 1
        if consonants == n:
            words_set.add((consonants, words[i][1]))
            
    # Sort the words_set based on the original index of the words 
    # and return the words in the words_set.
    words_set = sorted(list(words_set), key = lambda x: x[1])
    words = []
    for i in range(len(words_set)):
        words.append(words_set[i][0])
    return words
