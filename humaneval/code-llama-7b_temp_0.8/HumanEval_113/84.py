
def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3',"11111111"])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    """
    # Base Case: The list is empty
    if lst == []:
        return []
    # Base Case: The list has only one element
    if len(lst) == 1:
        return [lst]
    # Recursive Step: The list has more than one element.
    # Remove the first and last elements and add it to the list of odd count
    # of the first and last element respectively
    return [lst[0]] + odd_count(lst[1:len(lst)-1]) + [lst[-1]]
