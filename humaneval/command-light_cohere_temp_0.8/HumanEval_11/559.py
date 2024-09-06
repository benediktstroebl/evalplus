Here is a self-contained Python script that solves the problem you've described:
```python
def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings a and b consisting only of 1s and 0s.
    Return: '101010110'
    """
    return a ^ b

#Test case 1
test_case_1 = "010"
test_case_2 = "110"
test_case_3 = "100"

#Test case 2
test_case_4 = "101010110"
test_case_5 = "000"

#Test case 3
test_case_6 = "001010"

#Test case 4
test_case_7 = "101010101"

#Test case 5
test_case_8 = "101010"

#Test case 6
test_case_9 = "001111"

#Test case 7
test_case_10 = "10010101"

#Test case 8
test_case_11 = "100"

#Test case 9
test_case_12 = "1010"

#Test case 10
test_case_13 = "11"

#Test case 11
test_case_14 = "11001"

#Test case 12
test_case_15 = "1110"

#Test case 13
test_case_16 = "11100"

#Test case 14
test_case_17 = "11011"

#Test case 15
test_case_18 = "10110"

#Test case 16
test_case_19 = "1001111"

#Test case 17
test_case_20 = "100101010"

#Test case 18
test_case_21 = "10000100100"

#Test case 19
test_case_22 = "100000000"

#Test case 20
test_case_23 = "10"

print(string_xor(test_case_1, test_case_2)) # expected output: '100'

print(string_xor(test_case_3, test_case_4)) # expected output: '110'

print(string_xor(test_case_5, test_case_6)) # expected output: '0000'

print(string_xor(test_case_7, test_case_8)) # expected output: '100'

print(string_xor(test_case_9, test_case_17)) # expected output: '0000'

print(string_xor(test_case_10, test_case_19)) # expected output: '100'

print(string_xor(test_case_14, test_case_17)) # expected output: '00'

print(string_xor(test_case_20, test_case_23)) # expected output: '100'
```
This Python script defines a function `string_xor` that performs the XOR operation on two input strings, which are limited to consist only of the characters '1' and '0'. The script then includes several test cases to verify the correctness of the `string_xor` function.