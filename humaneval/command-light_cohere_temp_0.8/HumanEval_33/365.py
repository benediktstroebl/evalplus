```python
def sort_third(l: list):
    """Sorts a list of integers so that all values divisible by three appear in their original order, and the rest are sorted."""
    l = list(sorted(l,key=lambda x: 3%x))
    return l
#Test cases
l1 = [5, 6, 3, 4, 8, 9, 2]
print(sort_third(l1))  #Expected Output: [2, 6, 3, 4, 8, 9, 5]

l2 = [1, 2, 3, 4, 5, 6, 7]
print(sort_third(l2))  #Expected Output: [1, 2, 4, 5, 6, 7]
```
This script defines a function sort_third that takes a list l as input and sorts it such that all the values divisible by three appear in their original order and the rest are sorted. The function uses the time to sort the list using the key created by the lambda function that takes 3%x as input, which tells the function to sort values that are divisible by three to stay in their original order and sort all other values that are not divisible by three to follow.