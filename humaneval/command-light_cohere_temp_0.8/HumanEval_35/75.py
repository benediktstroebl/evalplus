```python
def max_element(lst):
    if not_num_max(lst) == float('-inf'):
        raise ValueError("The list is empty.")
    return lst[0]

def not_num_max(lst):
    if not lst:
        return float('-inf')
    return max(lst, key=lambda x: x)

if __name__ == "__main__":
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    print(f"The maximum element in {test_list} is: {max_element(test_list)}")
    test_empty = []
    print(f"The maximum element in {test_empty} is: {max_element(test_empty)}")
    test_negative = [-5, 3, -20]
    print(f"The maximum element in {test_negative} is: {max_element(test_negative)}")
```
The code defines two functions: `max_element` solves the problem, while `not_num_max` checks if the list is empty and returns `float('-inf')` if it is. This ensures the the use of a useful sentinel value. The main function tests a list-based input and prints the result of the `max_element` function for each test case.