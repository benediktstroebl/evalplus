
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
    # split string s into a list of substrings using space as a separator
    s_list = s.split()
    
    # sort the substrings in the list by their frequency of occurrence
    s_list.sort(key=lambda x: len(filter(lambda y: x == y, s_list)))
    
    # initialize the result list
    result = []
    
    # iterate over the sorted list of substrings
    for i in range(len(s_list)):
        # if the substring at index i has exactly n consonants
        if sum(ord(c) for c in s_list[i]) == n:
            # add the substring to the result list
            result.append(s_list[i])
    
    return result
