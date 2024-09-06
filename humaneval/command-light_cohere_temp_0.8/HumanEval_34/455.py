```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, '', '', '<<object ']]

if __name__ == "__main__":
    test_lst = [5, 3, 5, 2, 3, 3, 9, 0, 'a', 'bc', 123]
    print("unique:", unique(test_lst))
    test_str = '').join(['a'bar,'  b','c'])
    print("\nunique:", unique(test_str))
    test_int = [123, 456, 0]
    print("\nunique:", unique(test_int))
```
The provided Python code defines a function called unique that aims to return unique elements from an input list. It employs a specific behavior to filter out duplicates and empty values, and it uses a set to track elements that have already been seen. The code includes a main section with test lists and strings, showcasing the function's behavior by printing the results for different input scenarios.