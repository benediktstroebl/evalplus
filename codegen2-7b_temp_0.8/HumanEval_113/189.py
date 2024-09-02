
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
    odd_counter = 0
    odd_str_lst = []
    for elem in lst:
        odd_counter = 0
        for digit in elem:
            if digit == "0":
                odd_counter += 0
            elif digit == "1":
                odd_counter += 1
            elif digit == "2":
                odd_counter += 2
            elif digit == "3":
                odd_counter += 3
            elif digit == "4":
                odd_counter += 4
            elif digit == "5":
                odd_counter += 5
            elif digit == "6":
                odd_counter += 6
            elif digit == "7":
                odd_counter += 7
        odd_str_lst.append(odd_counter)
    return odd_str_
