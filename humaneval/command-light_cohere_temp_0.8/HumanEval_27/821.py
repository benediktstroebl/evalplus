```python
def flip_case(string):
    return ''.join(''.swapcase(string))

# Test case 1
print(flip_case('Hello'))
# Expected Output: hELLO

# Test case 2
print(flip_case('HELLO'))
# Expected Output: hEloO

# Test case 3
print(flip_case('hello'))
# Expected Output: HEllO
```
The function `flip_case` takes a string as input and returns a new string where the characters are swapped between lowercase and uppercase. It achieves this by using the Python's built-in `swapcase` method to convert each character to its corresponding case. The output of the function will be the same string, but with characters swapped between lowercase and uppercase.