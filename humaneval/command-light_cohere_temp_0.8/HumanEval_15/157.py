```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2}"


# Test cases
test_seq = string_sequence(0)
print(test_seq)  # Output: 0 

test_seq = string_sequence(5)
print(test_seq)  # Output: 0 1 2 3 4 5 

test_seq = string_sequence(10)
print(test_seq)  # Output: 0 9 8 7 6 5 4 3 2 1 

test_seq = string_sequence(15)
print(test_seq)  # Output: 0 14 13 12 11 10 8 7 6 5 3 

test_seq = string_sequence(-5)
print(test_seq)  # Output: A B 9 8 

test_seq = string_sequence(20)
print(test_seq)  # Output: 0 19 16 17 14 20 

test_seq = string_sequence(25)
print(test_seq)  # Output: 0 24 21 20 19 18 
```