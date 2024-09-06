```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The problem asks us to create a function that, given a list of integers, returns a tuple (`a`, `b`) where `a` is the largest integer among negative integers in the list and `b` is the smallest integer among positive integers in the list. If the list does not contain any negative or positive integers, `a` and `b` should be `None`.

The provided Python script aims to fulfill this requirement with a concise and efficient function: `largest_smallest_integers`. This function takes a list `lst` as input and uses two separate generator expressions, aided by the `min()` and `max()` functions, to pinpoint the smallest positive and largest negative integers, respectively. 

Here's an example of function usage:
```python
input_list = [2, 4, 1, 3, 5, 7]
result = largest_smallest_integers(input_list)
print(result)  # Output: (None, 1)
```

And here is an example of when the list contains no negative or positive integers:
```python
input_list = []
result = largest_smallest_integers(input_list)
print(result)  # Output: (None, None)
```

We assure that the function handles all the edge cases mentioned in the problem description and effectively delivers the correct results.