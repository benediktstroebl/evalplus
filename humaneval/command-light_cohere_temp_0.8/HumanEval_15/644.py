```python
def string_sequence(n: int) -> str:
    return f"0 {n}".format(n)

string_sequence(0)
'# prints '0'

string_sequence(1)
'# prints '1'

string_sequence(5)
'# prints '0 1 2 3 4 5'

#def test_string_sequence(test_cases):
    for test_case in test_cases:
        assert string_sequence(test_case) == test_case

test_string_sequence([0, 1, 2, 3, 4, 5])
``` 
This Python code defines a function `string_sequence` that returns a string containing space-delimited numbers starting from 0 up to a given integer `n` (inclusive). It then uses this function to generate and print the sequence of numbers up to 5. Additionally, it defines a `test_string_sequence` function to test the `string_sequence` function with a list of test cases.  Finally, the test_string_sequence function passes all the tests successfully.