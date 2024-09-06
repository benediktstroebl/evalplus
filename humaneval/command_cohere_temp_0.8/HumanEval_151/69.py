Here's a Python function that solves the given problem and includes concise test cases to verify its correctness:
```python
def double_the_difference(numbers):
    """
    Sum of squares of odd numbers in the list that are integers, ignoring negatives.

    :param numbers: List of numbers.
    :return: Sum of squares of odd integers.
    """
    odd_integers = [num for num in numbers if num % 2 != 0 and num >= 0 and isinstance(num, int)]
    return sum(num ** 2 for num in odd_integers)

# Test cases
empty_list = []
correct_result = 10
another_correct_result = 81
no_negative_result = 0

test_cases = [
    ([1, 3, 2, 0], correct_result),
    ([-1, -2, 0], no_negative_result),
    ([9, -2], another_correct_result),
    (empty_list, no_negative_result),
    ]

for numbers, result in test_cases:
    assert double_the_difference(numbers) == result
```

Let's break down the code:
1. **function definition**: `def double_the_difference(numbers): ...` provides a concise description of the function in the docstring.
2. **Filtering odd integers**: `odd_integers = [num for num in numbers if num % 2 != 0 and num >= 0 and isinstance(num, int)]` uses a list comprehension to filter odd integers from the input list. It also checks if the number is a positive integer.
3. **squaring and summing**: `return sum(num ** 2 for num in odd_integers)` squares each odd integer and returns the sum of these squares.
4. **Test cases**: `test_cases = [ ... ]` defines a list of test cases, including the input list of numbers and the expected result.
5. **Assertion checks**: `for numbers, result in test_cases:` iterates through each test case, and for each, asserts that `double_the_difference(numbers)` yields the expected `result`.

To verify the function, we can simply run the script, and the assertions will report any errors or differences between computed and expected results. 

You can add more test cases as needed to cover various scenarios and edge cases, ensuring the function's correctness. 

This code is a concise and self-contained solution to the problem, and each test case can be executed independently to validate the functionality.  If you intend to run only a specific test case, you can modify the `for` loop to execute only the desired test: 
 ```python
for numbers, result in [([1, 3, 2, 0], 10), ([9, -2], 81), ([-1, -2, 0], 0), ( [], 0 )]:
    assert double_the_difference(numbers) == result
``` 
However, running all tests ensures comprehensive validation.