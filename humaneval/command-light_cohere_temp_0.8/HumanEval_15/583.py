```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """ 
    return f"0 {n} {" + str(n+1) + "}"

# test cases
test_case_1 = 0 
test_result_1 = string_sequence(test_case_1)
assert test_result_1 == '0 0', "Test case 1 failed" 

test_case_2 = 5
test_result_2 = string_sequence(test_case_2)
assert test_result_2 == '0 5', "Test case 2 failed" 

test_case_3 = 100
test_result_3 = string_sequence(test_case_3)
assert test_result_3 == '0 100', "Test case 3 failed" 

print("All tests passed")
```