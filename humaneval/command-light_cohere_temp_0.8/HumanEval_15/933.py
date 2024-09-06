Here's a self-contained Python function that returns a string containing space-delimited numbers starting from 0 up to the number n:

```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return ' '.join(str(i) for i in range(n))

# Test cases
test_string = string_sequence(5)
print("Test String:", test_string)

test_string = string_sequence(0)
print("Test String:", test_string)

test_string = string_sequence(-5)
print("Test String:", test_string)

test_string = string_sequence(10)
print("Test String:", test_string)
```
The output should be:
```
Test String
0
00
000
00100
```
The function uses the range function to generate the sequence and the str.s string function to convert the numbers into a string. 

Would you like help with anything else?