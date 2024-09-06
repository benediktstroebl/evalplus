```python
def string_sequence(n: int) -> str:
    """ 
    Returns a string containing space-delimited numbers starting from 0 upto n inclusive. 
    """ 
    if n <= 0:
        raise ValueError("n should be a positive integer")
    if n == 1:
        return '0'
    sequence = [0]
    while len(sequence) < n:
        sequence.append(sequence[-1] + 1)
    return ' '.join(sequence)

#Test case 1
test_string = string_sequence(1)
print("Test case 1: ", test_string)

#Test case 2
test_string = string_sequence(5)
print("Test case 2: ", test_string)

#Test case 3
test_string = string_sequence(-5)
print("Test case 3: ", test_string)

#Test case 4
test_string = string_sequence(0)
print("Test case 4: ", test_string)

#Test case 5
test_string = string_sequence(10)
print("Test case 5: ", test_string)
```