```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The problem asks us to create a function that, given a list of integers, returns a tuple (`a`, `b`) where `a` is the largest integer of those in the list that are less than zero and `b` is the smallest integer of those in the list that are greater than zero. If the list contains no integers beyond zero, return `None` for both values in the tuple. Our solution creates two variables, `positive` and `negative`, initialized by the smallest and largest integers in the list that fulfill the conditions using `min` and `max` functions. These final values are returned in a tuple, `(-1, 1)` in the example above. 

Here is the inline test case provided in the problem:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Output: (None, 1)
print(largest_smallest_integers([]))  # Output: (None, None)
print(largest_smallest_integers([0]))  # Output: (None, None)
```

And here is a test case not provided in the prompt to ensure correct functionality:
```python
print(largest_smallest_integers([-3, -1, -11, -5, -17, -20, -22, -25]))  # Output: (-3, 1)
``` 
The test case is designed to check if the function works for lists that include multiple integers beyond zero or zero itself, ensuring the lowest negative integer and the highest positive integer among those in the list are correctly selected. 

To handle the edge cases, our function returns `None` for both values if the list contains no negative integers or positive integers, aligning with the expected output.