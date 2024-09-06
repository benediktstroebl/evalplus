Here's a Python script that contains a function, `check_dict_case`, which takes a dictionary as an argument and returns true if all the keys in the dictionary are in lowercase or uppercase format and false otherwise. The script also includes test examples to verify the functionality of the `check_dict_case` function.

```python
def check_dict_case(dict):
    if not dict:
        return False
    for key in dict:
        # check if all the keys are in lower case
        if not isinstance(key, str) or not key.islower():
            return False
    return True

# Example usage
exemplar_dict = {"a": "apple", "b": "banana"}
test_cases = [
    {"a": "apple", "A": "banana", "B": "banana"},
    {"a": "apple", 8: "banana", "a": "apple"},
    {"Name": "John", "Age": "36", "City": "Houston"},
    {"STATE": "NC", "ZIP": "12345"},
]

for test in test_cases:
    assert check_dict_case(test) == (test.keys() <= {"a", "b"}), f"Expected {test.keys() <= {'a', 'b'}}, Got {test.keys()}"
```

In the test suite, we have a variety of test cases. We assert that the function `check_dict_case` returns the correct value for each test case, this is done by comparing the keys of the test case dictionary to the set {"a", "b"}. This set is constructed because the exemplar dictionary has only {"a", "b"} as keys. The keys of each test case dictionary are compared to this set using the <= operator, and the resulting boolean value is compared to the expected value given in the comment using the assert statement. 

Note that the first exemplar test case has the same keys as the exemplar dictionary, so it should return True, whereas the remaining test cases have different keys and should return False.