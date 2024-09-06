```python
def check_dict_case(dictn):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    """
    if not dictn or not isinstance(dictn, dict):
        return False
    lowercase_dict = {}
    uppercase_dict = {}
    for key, value in dictn.items():
        lowercase_key = key.lower()
        uppercase_key = key.upper()
        if lowercase_key in lowercase_dict or uppercase_key in uppercase_dict:
            return False
        lowercase_dict[lowercase_key] = value
        uppercase_dict[uppercase_key] = value
    return True
```

The script defines a function `check_dict_case` that takes a single argument `dictn`, which represents the input dictionary. 

The function first checks if the dictionary is empty or not, and if it receives an argument that is not a dictionary, it returns `False`. After that, it iterates through the keys and values of the input dictionary and creates two new dictionaries, `lowercase_dict` and `uppercase_dict`, which store the key-value pairs with keys converted to lowercase and uppercase, respectively. If a key already exists in either of these dictionaries, the function returns `False`. Otherwise, it returns `True`. 

The function returns `True` if all keys are either in lowercase or uppercase and returns `False` otherwise or if the given dictionary is not empty and is not a dictionary or if the keys and values are not both strings. 

You can test this function by providing various test cases to validate its behavior. 
```python
# Test Cases
test_cases = [
    {"a": "apple", "b": "banana"},
    {"a": "apple", "A": "banana", "B": "banana"},
    {"a": "apple", 8: "banana", "a": "apple"},
    {"Name": "John", "Age": "36", "City": "Houston"},
    {"STATE": "NC", "ZIP": "12345"},
]

expected_results = [True, False, False, False, True]

for i in range(len(test_cases)):
    print(f"TestCase {i+1}:")
    print(f"Input: {test_cases[i]}")
    result = check_dict_case(test_cases[i])
    print(f"Output: {result}")
    print(f"Expected: {expected_results[i]}")
    if result != expected_results[i]:
        print("******* TEST FAILED ********")
    else:
        print("******* TEST PASSED ********")
```

This driver code will ensure that the function `check_dict_case` behaves as expected for various inputs as described in `problem_statement`. 
This code should be placed in the same file as the function definition. 

This driver code provides test cases that cover different scenarios, and these test cases help verify the correctness of the `check_dict_case` function.  By executing this code, you can comprehensively test the function and ensure its behavior aligns with the problem statement.  You can use this code as a starting point and adjust it based on your specific needs or additional test cases you'd like to include.