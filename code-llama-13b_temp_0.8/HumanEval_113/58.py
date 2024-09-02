
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

    # make a function that counts the odd numbers in a string
    def count_odd(s):
        num_odd = 0
        for i in s:
            if int(i) % 2 == 1:
                num_odd += 1
        return num_odd

    # new empty list to put the new string in
    new_lst = []
    # make a new string to append to the list
    for i in lst:
        new_string = "the number of odd elements " + str(count_odd(i)) + "n the str" + str(
            count_odd(i)) + "ng " + str(count_odd(i)) + " of the " + str(count_odd(i)) + "nput."
        new_lst.append(new_string)
    return new_lst

