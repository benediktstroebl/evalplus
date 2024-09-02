
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
    # you can use python's built-in sorted function to sort the characters
    # of the string and return a new string with the characters sorted in
    # the desired order.
    #
    # This will work for any type of character.
    #
    # Here's a simple example:
    #
    # s = 'Hello World!!!'
    # s = s.split()
    # s = sorted(s)
    # s = ''.join(reversed(s))
    #
    # but you can also use a list of sorted characters
    #
    # s = 'Hello World!!!'
    # s = s.split()
    # s = sorted(set(s))
    # s = ''.join(reversed(s))
    #
    # Here's another example:
    #
    # s = 'Python rocks!'
    # s = s.split()
    # s = sorted(set(s))
    # s = ''.join(reversed(s))
    #
    # You can use the code you provided above to do the same thing, but it
    # will be more efficient for large strings, since it only needs to perform
    # a single pass over the string, rather than multiple passes as would be the
    # case with the built-in `sorted` function.
    #
    # You can also use a list comprehension to achieve the same thing:
    #
    # s = 'Python rocks!'
    # s = s.split()
    # s = [c for c in s]
    # s = sorted(s)
    # s = ''.join(reversed(s))
    #
    # This will work as well:
    #
    # s = 'Python rocks!'
    # s = s.split()
    # s = [c for c in s]
    # s = sorted([ord(c) for c in s], reverse=True)
    # s = ''.join(reversed(s))
    #
    # Here's a more efficient version of the previous list comprehension:
    #
    # s = 'Python rocks!'
    # s = s.split()
    # s = [
