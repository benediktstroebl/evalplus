
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
    #Write code here

    a = sorted(s.split())
    for i in range(len(a)):
        for j in range(len(a[i])):
            for k in range(j+1,len(a[i])):
                if ord(a[i][j])>ord(a[i][k]):
                    a[i][j], a[i][k] = a[i][k], a[i][j]
    return " ".join(a)
