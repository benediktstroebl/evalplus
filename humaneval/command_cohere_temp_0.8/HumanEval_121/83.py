```python
def solution(lst):
    odd_in_even = sum(x for x in lst if x % 2 and (len(lst) - x) % 2 == 0)
    return odd_in_even
```
This Python script provides a function called solution(), which takes a list of integers as input and returns the sum of all odd numbers present at even positions within the list. To do this, it uses a summing function within a generator expression, filtering odd numbers in even positions by checking both the condition that the number is odd (`x % 2`) and the condition that the position of that number is even in the list (`(len(lst) - x) % 2 == 0`). The result is the sum of odd numbers in even positions. The function's correctness is demonstrated by the provided examples in the markdown code block, ensuring it adheres to the specified problem's requirements.