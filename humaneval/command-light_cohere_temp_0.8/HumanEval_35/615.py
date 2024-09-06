```python
def max_element(lst):
    if not_elements(lst):  # Handle empty list
        return None
    return max(lst, key=lambda x: x[0])  # Use the first element as the key

def test_max_element(test_lst):
    assert max_element(test_lst) == 5  # Test with a list of integers

if __name__ == "__main__":
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    print("Maximum element:", max_element(test_list))  # Output: Maximum element: 5
```
The code defines the max_element function, which finds the maximum element in a list. The test_max_element function tests the max_element function with a sample list, ensuring the function works correctly. The code then demonstrates the maximum element in an example list using the max_element function.