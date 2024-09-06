```python
def solution(lst):
    odd_in_even = sum(x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 1)
    return odd_in_even
```
This Python script defines a function called solution which takes a list lst as input. It uses a sum function to calculate the sum of odd numbers found in even positions in the input list. The condition i % 2 == 1 checks if the current index is even (1-indexed), and x % 2 == 1 checks if the current element is odd. The sum function with the enumerate function allows us to iterate through the list and calculate the sum of odd elements in even positions. The result is returned from the solution function. Overall, this solution follows the problem's constraint, as it only traverses the list once, without any explicit sorting or filtering of elements.