Here's a self-contained Python script that implements the `intersperse` function from the prompt: 

```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    numbers = list(numbers)  # Convert input list to a list of integers
    result = [x + y for x, y in zip(numbers, numbers[1:]) if y != None] + numbers
    return result

# Test cases
test_cases = [
    [], 4,  # Zero length list, should return empty list
    [1, 2, 3], 4,  # Two consecutive numbers, should return with separator
    [1, 4, 2, 4, 3]
]

# Function call and test results
for case in test_cases:
    print(intersperse(case, 4))
```

This script defines a function `intersperse` that separates pairs of consecutive elements in a list using a provided `delimiter`. The function works by creating a new list with the elements separated into pairs and then combines the original list with the separated elements. 

The script then provides a set of test cases and uses a loop to iterate over each case. The results are printed for each test case, demonstrating the functionality of the `intersperse` function.