```python
def solution(lst):
    odd_in_even = sum(x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 1)
    return odd_in_even
```
This Python script defines a function called solution which takes a list lst as input. This function returns the sum of all odd numbers in the list that appear in even positions. The sum is calculated using a list comprehension, which iterates through the list and selects only elements that meet the condition of being odd and appearing in even positions (i.e., index i is even and the element x is odd). The sum of these odd elements is then returned as the result.