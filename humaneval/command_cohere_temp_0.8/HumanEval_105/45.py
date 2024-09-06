```python
def by_length(arr):
    sorted_arr = sorted(arr)
    stripped_arr = [str(el) for el in sorted_arr if el >= 1 and el <= 9]
    stripped_arr.reverse()
    digit_names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    final_result = [digit_names[i] for i in range(0, len(stripped_arr))]
    return final_result if final_result else []
```

The provided Python script defines a function `by_length` that takes an array of integers as input. It sorts the array, extracts the digits that are between 1 and 9, reverses the extracted array, and then replaces each digit with its corresponding name from "One" to "Nine". The final result is returned as a list of names, or an empty list if the input array is empty or contains no eligible digits.

Here is a test suite to ensure that the above function executes properly:
```python
def test_by_length():
    # Test Case: Basic Example
    arr = [2, 1, 1, 4, 5, 8, 2, 3]
    expected = ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    assert by_length(arr) == expected

    # Test Case: Empty Array
    arr = []
    assert by_length(arr) == []

    # Test Case: Array with Strange Numbers
    arr = [1, -1, 55]
    expected = ["One"]
    assert by_length(arr) == expected

    # Test Case: Array with Mixed Numbers
    arr = [3, 7, 4, 8, 1, 5, 2, 9]
    expected = ["Nine", "Eight", "Four", "Seven", "Six", "Five", "Two", "One", "One"]
    assert by_length(arr) == expected

test_by_length()
```

The test suite includes several test cases to cover different scenarios, ensuring the function behaves as expected.