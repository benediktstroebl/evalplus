```python
def max_element(lst):
    if not_list(lst):  # Check if list is valid
        return "Input should be a list"
    if not len(lst):  # Check for empty list
        return "List is empty"
    return max(lst)  # Max element will be returned after checking

def test():
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    print("Max element:", max_element(lst))
    print("This passed the test!")

# Test the function
test()
```