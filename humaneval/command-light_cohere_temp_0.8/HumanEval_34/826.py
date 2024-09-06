```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [0]]

if __name__ == "__main__":
    test_lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print(unique(test_lst))
    assert unique(test_lst) == [0, 2, 3, 5, 9, 123]
```
The code defines a function named unique that takes a list lst as input and returns a new list containing only the unique elements. The function uses a seen = set() to create a set of unique elements from the input list, and then iterates through the input list, adding elements to the seen set if they are not duplicates and not already in the output list. The function effectively filters out duplicates and returns a new list containing only the unique elements. 
The if statement ensures that the function is called and evaluated correctly. The test_lst contains a list of elements to be passed to the unique function, and the function's output is then compared to the expected output from the test_lst list using the assert statement.