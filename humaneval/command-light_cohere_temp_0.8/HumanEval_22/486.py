Here's a solution that does the job:
```python
def filter_integers(values):
    return [num for num in values if isinstance(num, int)]

# Test cases
values1 = [1, 2, 3, 'abc', ]
values2 = [3.14, 5]
values3 = [1, 2, 3, 'a', 4, 5]

print(filter_integers(values1))  # Output: [1, 2, 3]
print(filter_integers(values2))  # Output: [3.14, 5]
print(filter_integers(values3))  # Output: [1, 2, 3, 'a', 4, 5]
```

This script defines a function called **filter_integers** that takes a list of values and returns a new list that contains only the integers from the input. It then passes these test cases to the function and the output is printed to the console.