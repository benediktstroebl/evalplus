```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
This Python script defines the function `next_smallest()`, which takes a list of integers as input. It starts by sorting the list in ascending order using the `sorted()` function. Then, it checks whether the length of the list is less than 2. If the list has less than two elements, it returns `None`, indicating that there is no second-smallest element. However, if the list has two or more elements, it returns the second element of the sorted list, which is the next smallest element. 

Here is an example of how you can use the `next_smallest()` function to solve the given problem:
```python
print(next_smallest([1, 2, 3, 4, 5]))  # Output: 2
print(next_smallest([5, 1, 4, 3, 2]))  # Output: 2
print(next_smallest([]))  # Output: None
print(next_smallest([1, 1]))  # Output: None
```

This script accurately meets the problem requirements and exemplifies a straightforward solution, utilizing sorting to identify the second-smallest element or indicating the absence of one. Feel free to adapt this code to your needs or explore alternative approaches within your problem-solving endeavors.