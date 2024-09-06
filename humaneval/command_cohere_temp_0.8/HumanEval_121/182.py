```python
def solution(lst):
    return sum(num for num in lst if num % 2 == 1 and lst.index(num) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function calculates the sum of all odd numbers present in even positions within the list. To accomplish this, it employs a list comprehension, iterating through each element in the input list `(lst)`. Within the comprehension, it evaluates each number `(num)` to determine if it is odd (`num % 2 == 1`) and whether it appears in an even position within the list (`lst.index(num) % 2 == 0`). The `index()` method is used to determine the position of each number in the list, as odd positions are indexed 0, 2, 4, etc., while even positions are indexed 1, 3, 5, etc. If a number satisfies both conditions, it is included in the sum calculated by the sum() function. 

The function returns the calculated sum of odd numbers in even positions and should be equivalent to the sum of odd numbers in even positions in the list provided in the example. 

This is a sample Markdown code block with a self-contained Python script that solves the given problem.