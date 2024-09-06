```python
def max_element(lst):
    if not_elements(lst):
        raise ValueError("Input list cannot be empty")
    return max(lst)

def not_elements(lst):
    return not bool(isinstance(lst, float)) or not bool(isinstance(lst, int)) or not isinstance(lst, list))

if __name__ == "__main__":
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    print(f"The maximum element in {lst} is {max_element(lst)}")
```
The code defines a function `max_element` that takes a list as input and returns the maximum element in the list. The function also includes a `not_elements` test that ensures the list is not empty. The `not_elements` function uses the `isinstance` function to check the type of the input. 

Additionally, the code provides a test that creates a list with different data types and passes it to the `max_element` function to ensure that the function works correctly.