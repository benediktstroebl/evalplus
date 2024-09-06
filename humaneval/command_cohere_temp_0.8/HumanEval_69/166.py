```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > 0:
            freq = lst.count(n)
            if freq >= n and (max_val < 0 or n > max_val):
                max_val = n
    return max_val if max_val > 0 else -1
```

This script defines a function 'search' which solves the problem as described in the markdown code block. It iterates through the list, counting the frequency of each integer, and keeps track of the maximum value seen so far (max_val). If a number greater than zero has a frequency equal to or greater than its own value, and this value is greater than the current max_val, it updates max_val. Finally, it returns the max_val if such a value exists, or -1 otherwise. 

To help understand the code, here is an explanation of the logic: 
This problem can be solved by iterating through the list and keeping track of the greatest integer that is greater than zero (let's call it 'max_val') and its frequency in the list ('freq'). If we find a number that is greater than zero, and its frequency is greater than or equal to its own value, we update 'max_val' if necessary. At the end of the iteration, we return 'max_val' if it is greater than zero, or -1 if no such integer is found. 

Note that the code assumes that the input list 'lst' only contains positive integers. If the list contains other data types or negative integers, the function may not return the expected results. As mentioned in the original prompt, the function expects the list to be non-empty. If the list is empty, the function will throw an infinite loop error due to the lack of elements to iterate over.