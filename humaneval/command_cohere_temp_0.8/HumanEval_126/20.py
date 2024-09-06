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
The function uses a simple dictionary (`dups`) to count the occurrences of each number in the list. If there's more than one occurrence of any number, the function returns False (indicating not sorted). Otherwise, it proceeds to check if the list is incrementally sorted in ascending order, using the `all` function to iteratively compare each element with the next one. This solution passes all the test cases provided in the prompt. 
This solution has a time complexity of `O(n)` and a space complexity of `O(n)` as it requires iterating the list twice, once for duplication check and once for sorting check, and utilizes an extra dictionary to store the elements. Faster solutions can be achieved using more advanced Python techniques like `collections.Counter` and generator expressions.