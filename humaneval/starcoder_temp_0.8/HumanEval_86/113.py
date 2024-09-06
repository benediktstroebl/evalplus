
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # Your code here
    # return ''.join(sorted(s))
    # This problem is solved by using a dictionary with keys as characters and values as their ascii values
    # for example : {a:97,b:98,c:99}
    # here I am using the length of string as key and the dictionary of characters and values as value
    # for example : {12:{a:97,b:98,c:99}}
    # then I am using the sorted function with the key parameter set to the length of string
    # to get the sorted character of the string and for the values of the sorted string I am using the index
    # to get the key of the dictionary which is the character and then using the dictionary to get the value
    # and finally joining the string and returning the result.
    string_dict = {}
    for c in s:
        string_dict[len(s)] = string_dict.get(len(s),{})
        string_dict[len(s)][c] = string_dict[len(s)].get(c,ord(c))
    sorted_chars = sorted(string_dict[len(s)])
    string_chars = ""
    for c in sorted_chars:
        string_chars += c
    return string_chars
