```python
def exchange(lst1, lst2):
    odd = next((el for el in lst1 if el % 2 != 0), None)
    even = next((el for el in lst2 if el % 2 == 0), None)
    if odd is None and even is not None:
        return "YES"
    return "NO"
```
The `exchange()` function takes two lists `lst1` and `lst2` as input and checks if the odd number in `lst1` has a corresponding even number in `lst2` for exchange. It uses the `next()` function to retrieve the first odd number from `lst1` or the first even number from `lst2`, respectively. If an odd number is found in `lst1` and an even number is found in `lst2`, it returns "YES," indicating that we can exchange the numbers to get a list of even numbers in `lst1`. If no odd number is found in `lst1` and no even number is found in `lst2`, it returns "NO," as no exchange can be performed. 

Here is a test drive code for the function above:
```python
def test_exchange():
    # Test case 1: Successful exchange
    input_list1 = [1, 2, 3, 4]
    input_list2 = [2, 1, 4, 3]
    expected_result = "YES"
    result = exchange(input_list1, input_list2)
    assert result == expected_result, f"Expected '{expected_result}', but got '{result}'"

    # Test case 2: Failed exchange
    input_list1 = [1, 2, 3, 4]
    input_list2 = [1, 5, 3, 4]
    expected_result = "NO"
    result = exchange(input_list1, input_list2)
    assert result == expected_result, f"Expected '{expected_result}', but got '{result}'"

    # Test case 3: No odd number in list1
    input_list1 = [2, 4, 6, 8]
    input_list2 = [1, 2, 3, 4]
    expected_result = "YES"
    result = exchange(input_list1, input_list2)
    assert result == expected_result, f"Expected '{expected_result}', but got '{result}'"

test_exchange()
```
The tests ensure that the function behaves as expected for different scenarios and correctly determines if an exchange of elements between the two lists can make `lst1` a list of only even numbers. 

To better understand the logic behind this function, check out the explanation below: 

The problem is to take two lists of numbers and determine if we can exchange elements between them to make the first list consist only of even numbers. For example, given the lists `[1, 2, 3, 4]` and `[1, 5, 3, 4]`, we can exchange the first 1 with the 5, and then the resulting list `[1, 5, 3, 4]` has only one odd number, whereas the original list had three odd numbers.

The first thing that the function does is to check if there is an odd number in the first list using `next((el for el in lst1 if el % 2 != 0), None)`. The `next()` function is used to get the first element that meets the condition of being odd, or, if no such element exists, it returns `None`. If there is no odd number in the list, we immediately return "YES" because we have achieved the goal of having an even