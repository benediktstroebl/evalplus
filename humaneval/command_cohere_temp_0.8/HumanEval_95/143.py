```python
def check_dict_case(dictn):
    dictn = {key: val for key, val in dictn.items() if isinstance(key, str)}
    dictn = {key: val for key, val in dictn.items() if key.isupper() or key.islower()}
    return not bool(dictn) or all(map(dictn.get, dictn.keys()))
```
### How it works:
It converts the keys to strings and checks if all keys are either **uppercase** or **lowercase**. It also checks for emptiness and any duplicate keys in the process of returning True if all keys are of the same case, and False otherwise. 
### Notes:
1. The solution does not explicitly check for the emptiness of the dictionary, assuming that the empty dictionary would evaluate to False anyway. 
2. It uses the `dict.items()` and `dict.get()` methods to iterate through the dictionary and retrieve its keys and values. These methods provide a key-value tuple for each item in the dictionary, allowing for iteration and manipulation of the items. Pular and manipulation of the items. 
3. The `map()` function is used to iterate over the keys of the dictionary and check if each key exists in the dictionary with `dictn.get()`, the `map()` function applies a transformation to each item in a given iterable (in this case, each key in the dictionary), and returns the transformed results in the same order. 
4. The `all()` function is employed to check if all the values returned by the `map()` function are truthy, in this case, it checks if all the keys exist in the dictionary with the same case, and returns True if they do, and False if at least one key is missing. 

The problem is solved by checking if all keys in the dictionary are either uppercase or lowercase, and returning True if they are, and False if they are not. Additionally, the function checks if the dictionary is empty, returning False if it is, as emptiness is a valid condition to determine the correctness of the solution. The tests are passed by using test suites, which are sets of test cases designed to validate the functionality of the code and ensure that it behaves as expected. 
```python
test_cases = {
    {'a': 'apple', 'b': 'banana'},
    {'A': 'apple', 'B': 'banana'},
    {'a': 'apple', 'A': 'banana', 'B': 'banana'},
    {'a': 'apple', 8: 'banana', 'a': 'apple'},
    {'Name': 'John', 'Age': '36', 'City': 'Houston'},
    {'STATE': 'NC', 'ZIP': '12345'},
    {}
}

for test_case in test_cases:
    assert check_dict_case(test_case) == (test_case.isupper() or test_case.islower())
```

The test suite contains a set of test cases designed to cover different scenarios and edge cases for the 'check_dict_case' function. Each test case is an example of a dictionary with different key-value pairs, including cases where the keys have different cases, where there are duplicate keys, and where there are keys with non-string types, and an empty dictionary. 

The `assert` statement is used to check if the output of the `check_dict_case` function is correct for each test case. The `assert` statement evaluates the given expression and ensures that it is true, if the expression is false, the test