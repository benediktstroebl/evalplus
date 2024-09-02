
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

    # We're returning a list of strings
    output = []

    # For each input, we're going to have one output
    for input in lst:

        # The output will be a string
        output_string = ""

        # For each digit, we're going to check if it's odd
        for digit in input:
            if int(digit) % 2 != 0:
                output_string += "the number of odd elements in the string {} of the input".format(digit)

        # At the end of the string, we're going to append this string
        output.append(output_string)

    # We're going to return our output
    return output

