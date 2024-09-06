
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
    count = {}
    for i in lst:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    result = []
    for i in count:
        if i % 2 == 1:
            result.append(str(i))

    return result

lst = [str(int(x) if x.isdigit() else "") for x in input().split()]
for i, j in zip(lst[::2], lst[1::2]):
    if j.find(i) == -1:
        print(j + " not in lst")