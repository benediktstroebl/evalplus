
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
    # s.split(" ")
    # print(s.split(" "))
    # c = 0
    # for i in s.split(" "):
    #     if len(i) < n:
    #         c += 1
    #     else:
    #         return c
    # if c == len(s.split(" ")):
    #     return "No word matches"

    w_list = []
    n_list = []
    cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    words = s.split()
    for w in words:
        #print(w, end=" ")
        n_list = []
        for c in w:
            if c in cons:
                n_list.append(c)
        # print(n_list)
        if len(n_list) == n:
            w
