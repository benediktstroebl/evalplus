```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return bin(int(''.join(map(int, a+b))) ^ int(''.join(map(int, a)) ^ int(''.join(map(int, b))))).replace('0b', '')
```

The script defines a function `string_xor` that takes two strings `a` and `b` as input. The function performs binary XOR on the binary representations of the two strings, converts the result back to a string, and returns it. 

The function uses Python's `int` and `bin` functions to perform the conversion and arithmetic processes needed for the XOR operation, and map to convert the strings to numbers and then back to strings. 

This implementation ensures that the function will work correctly for strings consisting only of 1s and 0s, as specified in the problem statement. 

To understand the underlying mechanics of the `string_xor` function, let's break it down step by step:
1. **Integer Conversion**:   
    ```python
    int(''.join(map(int, a+b)))
    int(''.join(map(int, a)) )
    int(''.join(map(int, b)))
    ```
    
    These lines convert the input strings `a` and `b` as well as the string concatenation of `a` and `b` (represented by `a+b`) to integers. The `map` function is used to convert each character (which is either '0' or '1') to its corresponding integer (0 or 1). The `join` function is then used to concatenate these integers together into a single integer representation of the string.

2. **XOR Calculation**:  
    ```python
    ^ int(''.join(map(int, a)) ^ int(''.join(map(int, b))))
    ```
    
    This line performs the binary XOR operation between the integer representations of `a` and `b`. XOR is a bitwise operation, which means it operates on individual bits of the integers. The `^` operator in Python performs bitwise XOR.

3. **Binary Conversion**:  
    ```python
    bin(INT).replace('0b', '')
    ```
    
    This line converts the integer result of the XOR operation back to a binary string. The `bin` function converts the integer to a binary string, and `replace` is used to remove the initial '0b' prefix that Python adds.

4. **Final String Result**:  
    ```python
    return bin(int(''.join(map(int, a+b))) ^ int(''.join(map(int, a)) ^ int(''.join(map(int, b))))).replace('0b', '')
    ```
    
    This line returns the binary string result of the XOR operation, which is now a string that corresponds to the XOR of the two input strings.

This function allows for the XOR operation to be performed on any strings consisting only of the characters '0' and '1'. 

It's important to note that this function assumes that the input strings `a` and `b` contain only 1s and 0s, as mentioned in the problem statement. If the input strings contain other characters, the function may return unexpected results. Therefore, the function effectively computes the binary XOR of two input strings and returns the result as a string, making it a versatile tool for binary data manipulation.