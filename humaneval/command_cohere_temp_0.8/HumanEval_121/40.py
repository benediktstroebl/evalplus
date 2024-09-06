```python
def solution(lst):
    odd_in_even = sum(x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 1)
    return odd_in_even
```
This Python script provides a function called solution(), which takes a list of integers as input and returns the sum of all odd numbers present in even positions in the list. To achieve this, it employs a list comprehension, iterating through each element in the list. If the current element is odd and it occurs in an even position (e.g., 2, 4, 6th position), it adds its value to the running total odd_in_even. The sum is then returned, providing the total of all odd elements in even positions in the input list.