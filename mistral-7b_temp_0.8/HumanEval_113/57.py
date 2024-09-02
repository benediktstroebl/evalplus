
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
    # Check if the element is odd or not
    count = []
    for i in lst:
        # Convert string to integer
        i = int(i)
        # Check the number is odd or even
        if i % 2 == 0:
            odd = 0
        else:
            odd = 1
        count.append(odd)

    # Output odd count
    for i in range(len(count)):
        print("the number of odd elements", count[i], "n the str", i, "n of the",
              i, "nput.")

    return count


