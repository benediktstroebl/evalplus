```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n}:{n+1}" * (n+1)

# Test case 1
test_case1 = 5
result = string_sequence(test_case1)
assert result == '0 5:6:7:8:9:10:11:12:13:14:15'

# Test case 2
test_case2 = 0
result = string_sequence(test_case2)
assert result == '0:0'

# Test case 3
test_case3 = 3
result = string_sequence(test_case3)
assert result == '0:1:2:3:'

# Test case 4
test_case4 = 100
result = string_sequence(test_case4)
assert result == '0:100:101:102:103:104:105:106:107:108:109:110:111:112:113'
```