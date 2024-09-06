```python
import stringmenu as tm

# Function to perform XOR operation on two strings
def string_xor(a: str, b: str) -> str:
    return tm.string_xor(a, b)

# Test case 1
test_case_1 = tm.test_cases.string(
    '010', '110')
print(test_case_1[0] + " = " + str_xor(test_case_1[0], test_case_1[1]))

# Test case 2
test_case_2 = tm.test_cases.add("160")
 "16")
test_case_2 = tm.test_cases.add("17")
 XOR "177")
print(test_case_2[0] + " = " + str_xor(test_case_2[1], test_case_2[2]))
```

This script defines a function `string_xor` that performs a XOR operation on two input strings and then tests the function with two test cases. The output will be the string that contains the result of applying the XOR operation to the two input strings.