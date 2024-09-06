Here's a Python script that implements the `by_length` function with a self-contained code block:
```python
def by_length(arr):
    digitally_sorted = sorted(arr, key=lambda x: [int(y) for y in str(x)])
    reverse_sorted = digitally_sorted[::-1]
    named_digits = [
        "One", "Two", "Three", "Four",
        "Five", "Six", "Seven", "Eight", "Nine"
    ]
    return [named_digits[i] for i in reverse_sorted if i <= 9 and i >= 1]
```

The provided solution is structured as follows:
1. **Digit Sorting:** The integers are sorted digit by digit. This is achieved using a lambda function as the sorting key. For each integer `x` in the input array, we convert it to a string, split it into individual digits (using a list comprehension), and then interpret each digit as an integer. This results in an array of digits, which is then sorted lexicographically. After sorting, any strange numbers are ignored since they would have been sorted to the beginning or end of the array due to their digits.
2. **Reverse Sorting:** The digitally sorted array is reversed, ensuring the digits are in reverse order.
3. ** Naming Digits:** The reverse-sorted digit array is mapped to its corresponding names from the `named_digits` list.

This approach ensures that the integers 1 to 9 are correctly reversed and named, while any strange numbers are ignored. The function returns the named digit array or an empty array if no valid digits are present.

Here is a simple test suite to ensure the function behaves as expected:
```python
def test_by_length():
    # Valid Input Cases
    assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    assert by_length([]) == []
    assert by_length([-1, 1, 55, 4, 5, 8, 2, 3]) == ["One"]

    # Edge Cases
    assert by_length([10, 20, 30]) == ["Ten", "Twenty", "Thirty"]
    assert by_length([0, 1, 2]) == ["Zero", "One", "Two"]

    # Additional Strange Cases
    assert by_length([100, 1, 2]) == ["One"]  # strangeness ignored
    assert by_length([11, 12, 13]) == ["Eleven", " Twelve", "Thirteen"]  # counts as digits
    assert by_length([3, 31, 32]) == ["Three", "Thirty-One", "Thirty-Two"]  # counts as digits
```

Note that the naming convention for the test functions follows the standard `test_function_name()` format.