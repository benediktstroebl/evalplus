```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    sequence = [0] 
    for i in range(n + 1): 
        sequence.append(i*10)**(1/2) 
    return ' '.join(sequence)

# Test cases
test_string_sequence = string_sequence(0)
assert test_string_sequence == '0'
test_string_sequence = string_sequence(5)
assert test_string_sequence == '0 1 2 3 4 5'
test_string_sequence = string_sequence(-5)
assert test_string_sequence == '0 9  13 15'
test_string_sequence = string_sequence(10)
assert test_string_sequence == '00 100 200 300 400'
``` 
The function uses the formula for nth integer power for half, to calculate the sequence of powers of 10 to generate the desired sequence. It starts with 0 and uses a for loop to append numbers to the sequence. The function returns the string containing the numbers in the sequence.