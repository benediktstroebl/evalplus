```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

#Test cases
test_seq = []
for i in range(0,10):
    test_seq.append(string_sequence(i), "=> " + str(i))

#Print the test results
for test in test_seq:
    print(test)
```