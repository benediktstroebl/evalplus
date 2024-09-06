```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [0]]

if __name__ == "__main__":
    test_lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print("Unique:", unique(test_lst))  # expected output: [0, 2, 3, 5, 9, 123]
``` 
This code defines a function unique that takes a list as an argument and returns a new list containing only the unique elements from the original list. The seen set is used to keep track of elements that have been encountered. The unique function uses ax method to generate the new list, which only includes elements that are not in the seen set and not 0.

The main part of the code runs the unique function with the test list and prints the resulting unique list.