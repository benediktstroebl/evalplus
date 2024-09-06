Here's a Python script that implements the `by_length` function with a self-contained code block:
```python
def by_length(arr):
    sorted_arr = sorted(arr, key = lambda x: 1 if x <= 9 else x)
    reversed_sorted_arr = sorted(sorted_arr, reverse = True)
    reversed_sorted_arr = [str(elem).replace('1', 'One', 1).replace('2', 'Two', 1).replace('3', 'Three', 1).replace('4', 'Four', 1).replace('5', 'Five', 1).replace('6', 'Six', 1).replace('7', 'Seven', 1).replace('8', 'Eight', 1).replace('9', 'Nine', 1) for elem in reversed_sorted_arr]
    return reversed_sorted_arr if reversed_sorted_arr != [] else []
```

The `by_length` function sorts the array with a sorting key that sorts digits from 1 to 9 to the top. Then it reverses the order and converts each digit to its name. The function returns the list of names or an empty list if the input array is empty. 

Here is a test suite to ensure the function behaves correctly:
```python
def test_by_length():
    # Test case 1: basic input, only digits
    assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]

    # Test case 2: empty array
    assert by_length([]) == []

    # Test case 3: strange numbers are ignored
    assert by_length([1, -1, 55]) == ["One"]

    # Test case 4: multiple occurrences of the same digit
    assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Two", "Two", "One", "One", "Four", "Five", "Eight", "Three", "Three"]

test_by_length()
```

Make sure to install the necessary dependencies (`pytest` and ` hypothesis `) to run the test suite. You can install them with pip command `pip install pytest hypothesis`.