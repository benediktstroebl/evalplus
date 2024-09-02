
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
    counts = [0 for _ in lst]
    for i, item in enumerate(lst):
        for j, num in enumerate(item):
            if num not in "1234567":
                break
            if num == "7" or num == "3":
                counts[i] += 1
                break
    return [f"the number of odd elements {count}n the str{count}ng {i} of the {j}put."
            for i, count in enumerate(counts)
            for j in range(2, 10
