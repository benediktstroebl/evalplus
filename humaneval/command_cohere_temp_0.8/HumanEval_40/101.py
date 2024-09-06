```python
def triples_sum_to_zero(lst):
    # Sort the list in non-decreasing order
    sorted_lst = sorted(lst)
    # Use a hashset to keep track of elements encountered during iteration
    encountered = set()
    for i in range(len(sorted_lst) - 2):
        a = sorted_lst[i]
        for j in range(i + 1, len(sorted_lst) - 1):
            b = sorted_lst[j]
            if a + b == sorted_lst[j + 1] and (a, b) not in encountered:
                encountered.add((a, b))
                if i + 1 < j and (b, a) not in encountered:
                    return True
    return False
```

The function works by first sorting the list in non-decreasing order. It then uses a hashset to keep track of elements encountered during iteration. The function iterates through the list, checking if the current element, together with the element `i + 1` seconds ahead, adds up to the element `i + 2` ahead. If they do, and they haven't been encountered before, then they are added to the hashset. The function returns True if two pairs of elements are found that satisfy the condition. Otherwise, it returns False.

This algorithm takes advantage of the sorted nature of the list to avoid duplicates and improve performance. It uses a hashset to efficiently keep track of encountered elements and checks if both orders of pairs lead to a sum of zero, which is necessary for the problem's correctness.