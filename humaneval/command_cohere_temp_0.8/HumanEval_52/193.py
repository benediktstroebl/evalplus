```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x`, comparing it to the threshold `t` using the `<` operator. The `all()` function returns `True` if all comparisons are `True`, indicating that all numbers in the list are below the threshold, otherwise `False`. 

Here is a test case to ensure the function runs correctly:
```python
tested = below_threshold([1, 2, 4, 10], 100)
assert tested == True

tested = below_threshold([1, 20, 4, 10], 5)
assert tested == False
```
These tests check if the function returns the expected outputs, based on the problem's test cases.

The reasoning behind the solution is simplistic comparison using Python's list comprehension and the `all()` function. Let's walk through it:
1. List Comprehension: In one line, it compares each element in the list with the threshold and yields a Boolean value.
2. `all()`: This function takes an iterable of Boolean values (True/False) and returns True if all the values in the iterable are True. In other words, it's like "ANDing" all the Boolean values together. 
3. Thus, if all elements in the list are below the threshold, the expression after the `all()` would be True, and the function returns True. Otherwise, it returns False. In essence, the function leverages Python's built-ins to provide a concise and efficient solution.