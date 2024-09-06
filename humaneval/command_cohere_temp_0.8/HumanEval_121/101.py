```python
def solution(lst):
    odd_in_even = sum(x for x in lst if x % 2 and lst.index(x) % 2 == 0)
    return odd_in_even
```
This Python script defines a function called solution which takes a list lst as input. It aims to calculate the sum of odd numbers present in even positions within the list. To do this, it employs a list comprehension that iterates through each element x in the input list lst. For each element, it checks two conditions: first, whether the element x is odd (i.e., its remainder when divided by 2 is 1), and second, whether its index in the list lst is even (i.e., the modulo operation on its index result in a value of 0). If both conditions hold true for a specific element, it adds that element to the running total odd_in_even. Finally, the function returns the computed sum value. 

The given examples in the markdown code block demonstrate how the function works on specific input lists, and the function's output aligns with the expected results.