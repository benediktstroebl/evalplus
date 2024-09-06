```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    
    for num, count in dups.items():
        if count > 1:
            return False
    
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
The function uses a simple dictionary (`dups`) to count the occurrences of each number in the list. If there's more than one occurrence of a number, the function returns `False` immediately. After processing the list, if there are no duplicates, it proceeds to check if the list is sorted by iterating through all adjacent pairs of numbers and returning false if any inequality is found. 

The above solution is efficient beyond the given test cases, with a time complexity of O(n) and a space complexity of O(n). 

The markdown code block describes a function that takes in a list of numbers and returns `True` if the list is sorted in ascending order and does not contain more than one duplicate number. If the list has more than one duplicate number, the function returns `False`. The function is written in Python and can be easily installed and used.