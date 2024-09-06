
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
    result = []
    length = len(lst)
    for i in range(length):
        odd_count_list = []
        odd_count_list.append(lst[i % length])
        for j in range(1, len(lst) - i):
            if odd_count_list[-1] * 2 > odd_count_list[-2]:
                odd_count_list[-1] += 1
            odd_count_list.append(odd_count_list[-1])
        result.append("the number of odd elements " + str(odd_count_list[-1]) + "n the str" + str(odd_count_list[-2]) + " of the " + str(length) + "nput.")
    return result

lst = [digit.zfill(4) for digit in input().split()]
