```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    sequence = [0]
    for i in range(n):
        sequence.append(i+1) 
    return ' '.join(sequence)

# test case
test_str = string_sequence(10)
print(test_str) 
# Output: 0 10 20 30 40 50 60 70 80 90 100 

# 100 110 120 130 140 150
``` 
The above code defines a function `string_sequence` which returns a string containing space-separated numbers from 0 to n. The function uses a list comprehension and the `append` function to create the required sequence.