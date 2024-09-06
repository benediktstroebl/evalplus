```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This Python script provides a function called `next_smallest(lst)` that aims to return the second smallest element in a given list of integers `lst`. First, the function sorts the input list in ascending order using the built-in `sort()` method. Then, it checks the length of the list. If the length is less than 2, indicating that there is no distinct second smallest element, the function returns `None`. Otherwise, it returns the second element from the end of the sorted list, which is the second smallest element in the original list, ensuring that the problem requirements are correctly met. 

Here is a simpler alternative problem solution using Python:
```python
def next_smallest(nums):
    return nums[1] if len(nums) > 1 and nums[1] < nums[0] else None
```
This alternative approach directly checks the list `nums` to determine if it contains two elements and if the second element is smaller than the first. If these conditions are met, it returns the second element, otherwise, it returns `None`. This method eliminates the need for sorting and provides a more direct solution to the problem.