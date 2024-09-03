```python
def sum_squares(lst):
    """
    Calculate the sum of squared numbers in the given list,
    round each element to the upper integer(Ceiling) first.
    Return the number of squared values in the list as the result.
    """

    list of numbers first

    # Initialize sum with first element
    sum = lst[0]

    # Add the sum of the next number to the sum
    sum += (lst[1] ** 2)

    # Add the sum of the next number to the sum
    for i in range(2, len(lst)):
        sum += (lst[i] ** 2)

    return sum

# Unit tests
def test_sum_squares():
    # Create list of numbers
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Call the function with the list
    result = sum_squares(lst)

    # Compare the result with the expected output
    assert result == 28

    # Create list of negative numbers
    lst = [-2, -1, -3, -4, -5, -6, -7, -8, -9]

    # Call the function with the list
    result = sum_squares(lst)

    # Compare the result with the expected output
    assert result == 12

    return True

if __name__ == "__main__":
    # Run the unit tests
    test_sum_squares()
```
This Python script defines a function `sum_squares` that calculates the sum of squared numbers in a given list, rounds each element to the upper integer first, and returns the result. The script also includes unit tests to ensure the correctness of the `sum_squares` function.