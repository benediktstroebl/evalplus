
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
    # Write your code here
    word_list = []
    word_counter = []
    s_array = []
    for i in range(len(s)):
        if s[i] != ' ':
            s_array.append(s[i])
        else:
            if len(s_array) == 1:
                if s_array[0] in 'aeiouAEIOU':
                    s_array = []
                else:
                    word_list.append(s_array)
                    word_counter.append(s_array.count(s_array[0]))
                    s_array = []
            else:
                if s_array[0] in 'aeiouAEIOU':
                    s_array = []
                else:
                    word_list.append(s_array)
                    word_counter.append(s_array.count(s_array[0]))
                    s_array = []
    if len(word_list) == 0:
        return word_list
    else:
        new
