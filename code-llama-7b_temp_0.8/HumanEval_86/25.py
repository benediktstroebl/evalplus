
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
    # YOUR CODE HERE
    s1 = s.split()
    s2 = []
    for word in s1:
        s3 = ""
        for char in word:
            s3 += chr(ord(char))
        s2.append(s3)
    s2.sort()
    s4 = ""
    for word in s2:
        s4 += word + " "
    return s4[:-1]
