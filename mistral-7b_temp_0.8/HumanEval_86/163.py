
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
    # return "".join(sorted(list(s)))

    # l = [word.lower() for word in s.split(" ") if word]
    # l2 = ""
    # for i in range(len(l)):
    #     l2 += l[i]
    #     for j in range(1, len(l[i])):
    #         l2 += (chr(ord(l[i][j]) + 1) if ord(l[i][j]) < ord(l[i][j-1]) else chr(ord(l[i][j]) - 1))
    # print(l2)
    # return l2

    s = " ".join([sorted(word) for word in s.split(" ")])
    return s

