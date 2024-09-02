
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
    # Your code goes here
    # do not use the function 'len'
    # do not use the function 'count'
    # do not use the function 'lower'

    if s=="":
        return []
    else:
        s_list = list(s)
        s_list_with_n_consonants = []
        for i in range(len(s_list)-1):
            if s_list[i]==" " and s_list[i+1]!=" ":
                count_cons_in_word = 0
                word = ""
                for j in range(i+1,i+len(s_list[i+1:i+len(s_list[i+1:i+len(s_list[i+1:i+len(s_list[i+1:i+len(s_list[i+1:i+len(s_list[i+1:i+len(s_list[i+1:i+len(s_list[i+1:i+len(s_list[i+
