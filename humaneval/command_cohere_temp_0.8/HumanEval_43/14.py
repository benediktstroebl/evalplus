```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0:
            twin = -i
            if twin in seen:
                return True
            seen.add(i)
        else:
            # Ignore negative integers
            continue
    return False
```

This Python script defines a function pairs_sum_to_zero that takes a list l as input. It then iterates through the list, checking if the absolute value of each integer is already in the set seen. If it is, this indicates the presence of a twin with a value that negates the original integer, resulting in a sum of zero. The function returns True in such cases. If the loop completes without finding a pair that sums to zero, the function returns False. This solution is efficient with a time complexity of O(n), where n is the length of the input list.