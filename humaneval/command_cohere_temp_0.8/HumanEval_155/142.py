Here's a Python script that contains a function called even_odd_count that takes an integer num as input and returns a tuple with the number of even and odd digits respectively. This function is designed to solve the problem you've described:
```python
def even_odd_count(num):
    if not isinstance(num, int):
        return "Input should be an integer"
    
    count_even = 0
    count_odd = 0
    
    str_num = str(num)
    
    for char in str_num:
        if char == '0' or char == '1' or char == '2' or char == '3':
            if char % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        else:
            return "Invalid input. Input should be an integer."
    
    return (count_even, count_odd)

# Example usage
print(even_odd_count(-12))  # Output: (1, 1)
print(even_odd_count(123))   # Output: (1, 2)
```

This implementation iterates through each digit in the decimal representation of the number and counts the number of even and odd digits. It then returns a tuple with these two counts. The input validation ensures that only valid integer inputs will be processed by the function. 

Let's break down the code step by step:
1. **Function Definition**: 
   ```python
   def even_odd_count(num):
       ```
   This line defines a function called `even_odd_count` that takes one parameter, `num`. The function is designed to solve the problem of counting even and odd digits in an integer.
2. **Input Validation**: 
   ```python
   if not isinstance(num, int):
       return "Input should be an integer"
   ```
   This condition checks whether the input `num` is an instance of the `int` class (i.e., it checks if it's an integer). If it's not, the function will return the string "Input should be an integer" indicating the invalid input. 
3. **Initialization of Counter Variables**: 
   ```python
   count_even = 0
   count_odd = 0
   ```
   These lines initialize two counters, `count_even` and `count_odd`, both set to zero. These counters will be used to keep track of the number of even and odd digits, respectively.
4. **Conversion to String**: 
   ```python
   str_num = str(num)
   ```
   This line converts the input integer num to a string, so we can work with its digital representation. 
5. ** DIGIT FLOW STATEMENT **:
   ```python
   for char in str_num:
   ```
   This is a loop that iterates through each character (digit) in the string `str_num`. 

6. **Digit Analysis**: 
   
   Inside the loop, it checks each digit as it iterates through the string: 
   ```python
   if char == '0' or char == '1' or char == '2' or char == '3':
       if char % 2 == 0:
           count_even += 1
       else:
           count_odd += 1
   ```
   Here, we check if the current digit `char` is one of '0', '1', '2', or '3'. If it is, we check whether it's even (divisible by 2) or odd, and increment the appropriate counter accordingly. 
7. **Invalid Input Handling**: 
   ```python
   else:
       return "Invalid input. Input should be an integer."
   ```
   If the loop encounters a