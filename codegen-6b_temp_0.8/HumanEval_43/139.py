

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    result = set()
    value_count = {}
    for elem in l:
        if elem in value_count:
            value_count[elem] += 1
        else:
            value_count[elem] = 1
    for elem in l:
        if elem not in result:
            result.add(elem)
        else:
            if value_count[elem] > 1:
                result.remove(elem)
    if 0 in l:
        result.remove(0)
    return len(result) == 2

test_pairs_sum_to_zero = ["pairs_sum_to_zero([1, 3, 5, 0])", "False", "pairs_sum_to_zero([1, 3, -2, 1])", "False", "pairs_sum_to_zero([1, 2, 3, 7])", "False", "pairs_sum_to_zero([2, 4, -5, 3, 5, 7])", "True", "pairs_sum_to_zero([1])", "False"]

for line in test_pairs_sum_to_zero:
	if pairs_sum_to_zero(eval(line)):
		print("true")
	else:
		print("false")