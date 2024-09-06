Here's a self-contained Python script with a function that sorts and validates a list of numbers in markdown code blocks:
```python
# Function to sort and validate a list of numbers in ascending order
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    # Convert input string into a list of numbers
    numbers = [float(num) for num in numbers.
    # Sort the started at index 0 and ascending
    numbers.sort_numbers = sorted(numbers)
    numbers = ' '.join(str(num) for num in numbers)
    return numbers

# Test cases
test_cases = [
    "three one five",
    "zero two three",
    "one two three four five six seven eight nine"
]

# Function call and result validation
results = sort_numbers(test_cases)

# Print results and compare to expected output
print(f'Test Cases: { results, "Expected Output":}")
for i, (tc, expected) in enumerate(zip(test_cases, ["Expected Output".split() + [""]), 2)):
    print(f"Test {i+1}: {tc} == {expected}")
```
This script defines a function `sort_numbers` that sorts and validates a list of numbers in ascending order. The function first converts the dry the list from the input string. The `test_cases` list contains test cases with corresponding expected outputs, and the `results` variable holds the actual output of the `sort_numbers` function call. The script validates the result by comparing the printed results with the expected output for each test case.