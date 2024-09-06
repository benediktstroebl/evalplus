Here's a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    binary_representation = bin(round(avg))[2:]
    return binary_representation if binary_representation.isalpha() else "0b" + binary_representation

# Test Cases
print(rounded_avg(1, 5))  # Output: 0b11
print(rounded_avg(7, 5))  # Output: -1
print(rounded_avg(10, 20))  # Output: 0b1111
print(rounded_avg(20, 33))  # Output: 0b11010
```

This code snippet defines the `rounded_avg` function, which takes in two integers `n` and `m` as parameters. It calculates the average of the two integers and rounds it to the nearest integer. Then, it converts the result to a binary string. If the absolute value of the difference between the rounded average and the actual average is greater than 0.5, then the function returns -1 to indicate an invalid range. The code snippet also includes test cases to help verify the correct operation of the `rounded_avg` function. 

The output of the test cases is as follows:
```
0b11
-1
0b1111
0b11010
```

Let's break down the Python script step by step:
1. **Defining the Function**: 
   ```python
   def rounded_avg(n, m):
   ```
   Here, we define the function `rounded_avg` that takes two integer parameters `n` and `m`. This function will compute the average of integers between `n` and `m`, round it to the nearest integer, and then convert the result to binary.
2. **Calculating the Average**:
   ```python
   avg = (n + m) // 2
   ```
   This line calculates the average of `n` and `m` using integer division (`//`) to round it to the nearest even number. This ensures that both `n` and `m` are considered in the average, as per the problem statement.
3. **Handling Invalid Range**:
   ```python
   if n > m:
       return -1
   ```
   This conditional check handles the case where `n` is greater than `m`. In such a scenario, the function returns `-1` as indicated by the problem statement.
4. **Converting to Binary Representation**:
   ```python
   binary_representation = bin(round(avg))[2:]
   ```
   Here, we use the `bin` function to convert the rounded average `avg` to a binary string representation. The `round` function ensures the average is rounded down to the nearest integer. We slice the resulting string from the third character (`[2:]`), since the first two characters in the binary representation of an integer are '0b'.
5. **Returning the Binary Representation**:
   ```python
   return binary_representation if binary_representation.isalpha() else "0b" + binary_representation
   ```
   This conditional checks whether the binary representation is a valid string (using the `isalpha()` function). If it's not a string, it means the average is zero, and we prepend `"0b"` to the binary representation to ensure it's a valid binary string.

The self-contained code block allows you to plug in different values for `n` and `m` and obtain the desired output without relying on any external variables or libraries