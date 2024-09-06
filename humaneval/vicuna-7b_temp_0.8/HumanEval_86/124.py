
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
    # One way to solve this problem is to use Python's built-in
    # sorting function, sort.
    # Convert the string to a list of words
    # Use sort() function on the list of words
    # Join the words back to form the string
    # The sorted list will be in the order of the characters
    # So, we need to reverse the order to get the original order
    # This approach will work but it is not efficient for large string
    # So, we can use Trie data structure which is more efficient for this problem
    # You can implement Trie in python by using the following code
    # import re
    # trie = re.compile(r'(?i)(\w+|[^\w\s])')
    # trie.findall(s)
    # convert to list and sort it
    #join the list to get the final string
    # Your code here
    pass