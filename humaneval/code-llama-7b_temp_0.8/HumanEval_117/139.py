
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
    #s = s.split()
    #print(s)
    #n = int(n)
    #if len(s) == 0:
    #    return []
    #else:
    #    result = []
    #    for w in s:
    #        if len(w) == n:
    #            result.append(w)
    #    return result
    
    #words = s.split()
    #count = 0
    #word_list = []
    #while count < n:
    #    for word in words:
    #        if word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u':
    #            continue
    #        else:
    #            count += 1
    #            word_list.append(word)
    #    if count < n:
    #        return []
    #return word_list
    
    if n < 0:
        return []
    if len(s) == 0:
        return []
    word_list = []
    for w in s.split():
        if len(w) == n:
            word_list.append(w)
    return word_list
    
    
    
