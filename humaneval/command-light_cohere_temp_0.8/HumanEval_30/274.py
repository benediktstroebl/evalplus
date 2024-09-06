```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases
tests = {
    "get_positive([-1, 2, -4, 5, 6]) -> [2, 5, 6]",
    "get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) -> [5, 3, 2, 3, 9, 123, 1]",
    "not pos -> []",
    "get_positive([]) -> []",
}

for case, expected in tests.
```fill_positive = get_positive

print(f"Test case {case}: {expected}")
for num in fill_positive(case):
    print(f"{num}")
``` 
This code defines a function called `get_positive` that takes a list as input and returns a new list containing only the positive elements from the original list. The function uses list comprehension to filter out the positive elements, and the result is then returned. 

Additionally, there are test cases defined, and the code iterates over each test case and passes each one to the `get_positive` function. The expected output for each test case will be printed.