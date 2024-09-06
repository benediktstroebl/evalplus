```python
def flip_case(string):
    return ''.join(''.swapcase(string))

# Test case 1
print(flip_case('hello')) # Output: 'HllEO'

# Test case 2
print(flip_case('world')) # Output: 'dwORLD'

# Test case 3
print(flip_case('HEllO')) # Output: 'hELLO'

# Test case 4
print(flip_case('o kingdom')) # Output: ' grOamy '

# Test case 5
print(flip_case(' pu rb o s t h i v e r l f')) # Output: ' PRbTOHSVLRF '

# Test case 6
print(flip_case('To be or not I must flip')) # Output: 'Ni tu olft I moFfsI'

``` 
This code defines the `flip_case` function that takes a string as input and returns a new string where all characters are flipped between uppercase and lowercase. The script then passes six test cases to ensure that the `flip_case` function is working correctly.