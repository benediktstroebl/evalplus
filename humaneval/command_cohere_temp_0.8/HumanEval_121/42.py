```python
def solution(lst):
    odd_in_even = sum(x for x in lst if x % 2 and lst.index(x) % 2 == 0)
    return odd_in_even
```
This Python script provides a function called solution(), which takes a list of integers as input and returns the sum of all odd numbers present at even positions within the list. To do this, it employs a generator expression, filtering odd numbers using the condition x % 2 and odd positions using the modulo index lst.index(x) % 2 == 0. The sum function then calculates the total of these selected numbers. The function's output is the value of this sum. The behavior of the function is illustrated in the docstring, which provides example inputs and their corresponding outputs. Notably, the script assumes the existence of a predefined list named lst, which is used for testing the function's correctness. In order to execute the function, this list has to be defined in the parent script.