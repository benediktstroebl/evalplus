```python
def string_sequence(n: int) -> str:
    if n == 0:
        return '0'
    sequence = [i for i in range(n)]
    return ' '.join(str(x) for x in sequence)

# Test case
test_seq = string_sequence(5)
print(test_seq)
# Output will be: 0 1 2 3 4 5 

# Test case 2
test_seq = string_sequence(10)
print(test_seq)
# Output will be: 0 9 8 7 6 5 3 2 1 

```