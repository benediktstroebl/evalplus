```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    for n, count in dups.items():
        if count > 1:
            return False
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
The function uses a simple dictionary (`dups`) to keep track of the occurrences of each number in the list. If there's a number more than once in the list, it increments its count in the dictionary; otherwise, it initializes the count to 1. Then, it checks if any of these counts are more than 1, returning `False` if so, as per the problem's statement. Lastly, it checks if the list is sequentially sorted with a quick iterative check using the `all` function and a lambda function for inequality. The `all` function iterates through all pairs of elements in the list except for the last one (as it only needs to check ordering up to the second-to-last element), with the lambda function quickly checking if the current element is less than or equal to the next.