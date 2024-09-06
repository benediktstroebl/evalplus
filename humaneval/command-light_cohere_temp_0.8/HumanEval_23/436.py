Here's a solution:

def strlen(string: str) -> int:
    """ Return length of given string
    Returns length of the given string"""
    return len(string)

#Test case 1
assert strlen('') == 0

#Test case 2
assert strlen('abc') == 3

In this solution, the strlen() function takes a string as an argument and returns its length using the built-in function len(). The test cases ensure the correctness of the function by passing different strings.