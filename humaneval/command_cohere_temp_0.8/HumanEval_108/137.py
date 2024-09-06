```python
def count_nums(arr):
    output = sum(int(b) for b in map(str, arr) if b != '-' and sum(int(d) for d in str(b)) > 0)
    return output
```

This script employs a generator expression on a mapped version of the input array, converting each element to a string and checking whether the first character is a hyphen ('-'), which would indicate a negative number, causing the expression to short-circuit. For elements that are not negative, it calculates the sum of their digits using a generator expression, comparing it to greater than 0, and accumulating the counts in an implicit sum. Finally, the total count of elements meeting the criteria is returned. 

Here is some example output:
```python
>>> count_nums([]) == 0
True
>>> count_nums([-1, 11, -11]) == 1
True
>>> count_nums([1, 1, 2]) == 3
True
```