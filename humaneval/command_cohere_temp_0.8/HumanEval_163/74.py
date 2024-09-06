```python
def generate_even_digits(a, b):
    """
    Generating even digits between two positive integers, in ascending order.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits from the range a to b, in ascending order.
    """
    # Ensuring the inputs are integers and sorting them for reference.
    a, b = map(int, (a, b))
    ab_str = f'{a}_{b}'
    sorted_ab_str = f'{a}_{b}'

    # Using integer manipulation to filter and sort even digits.
    even_digits = [int(d) for d in ab_str if d.replace('.', '', 1).isdigit() and d % 2 == 0]
    sorted_even_digits = sorted(even_digits)
    return sorted_even_digits
```

The function leverages the fact that integers are strings under the hood, to employ string manipulation techniques for efficient even digit extraction and sorting, eliminating the need for unnecessary intermediate conversions. 

The tests should reflect the following:
1. Testing with Various Pairs of Positive Integers:
   - Valid Inputs: `a = 2, b = 8`; `a = 8, b = 2`; `a = 10, b = 14`
   - Expected Outputs: `[2, 4, 6, 8]`; `[2, 4, 6, 8]`; `[]` respectively.

2. Testing Edge Cases:
   - `a = 1, b = 10`: Expect output to not include the single digit '1'.
   - `a = 10, b = 1`: Expect output to not include the single digit '1'.
   - `a = 0, b = 2`: Expect output to not include '0' or '2'.
   - `a = -1, b = 1`: Ensuring negative numbers do not affect the result.

3. Testing Empty Range:
   - `a = 100, b = 99`: Ensuring the output is empty for an unnecessary range.

Ensure you have appropriate test cases to cover all edge scenarios and adhere to the problem's guidelines. 
For optimal efficiency under the hood, this code uses a combination of string manipulation and Python's powerful `map` and `int` functions, eliminating the need for additional lists or intermediate variables.

It's important to note that this solution assumes the input integers only include digits and dots, and it's generally recommended to handle more complex number formats or edge cases separately if needed. A good self-contained solution should not only solve the immediate problem but also be modular and readable for potential reuse and extensibility.  If the problem allows, it's always good to add comments and docstrings to make the code more understandable.  A well-documented solution can be easily extended for future use or even shared with others to solve related problems.  Finally, testing is crucial to ensure the solution works correctly across different scenarios.  Ideally, the test cases should cover not only the happy path but also various edge cases to verify the robustness of the solution.  By following these guidelines, we can create a self-contained, efficient, and robust Python script.  Assuming you're working in a Jupyter environment, you can even add a cell with the following code to test the script instantly:
```python
test_cases = [
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
    (1, 10, []),
    (10, 1