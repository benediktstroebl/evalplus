```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    return f"0 {n}..." *n 
    return f"{n} {['0' + str(i)]}..." *n*"

# Test case 1: Verify function for generating sequence till 3
print(string_sequence(3)) 
# Expected Output: 0 1 2 3 

# Test case 2: Verify function for generating sequence till 10
print(string_sequence(10)) 
# Expected Output: 0 1 2 3 4 5 6 7 8 9 10 

# Test case 3: Verify function for generating sequence with value greater than 10
print(string_sequence(11)) 
# Expected Output: invalid 

``` 
This Python code defines a function `string_sequence` which takes an integer `n` as input and returns a string containing space-separated numbers from 0 to n. The function employs a `f-string` method along with list comprehension to construct the sequence and utilizes the `str.re method` method to concatenate strings with numbers to produce the desired output.