```python
def count_nums(arr):
    output = sum(int(b) for b in map(str, arr) if b != '-' and sum(int(d) for d in str(b)) > 0)
    return output
```
This Python script defines the function `count_nums`, which takes an array of integers as input and calculates the number of elements whose digit sum is greater than 0. To do this, it uses a list comprehension that iterates through each element in the input array, converts it to a string, and checks if the first character is not '-' (to avoid negative numbers). For each valid integer, it computes the sum of its digits using a generator expression within the sum function, and if this sum is greater than 0, it contributes to the total count. The function returns the final count of such elements.

Here is the explained breakdown of the code:
1. `def count_nums(arr)`: This line defines a function named count_nums that takes one parameter, arr, which is expected to be a list of integers.
2. `output = sum(int(b) for b in map(str, arr) if b != '-' and sum(int(d) for d in str(b)) > 0)`: This line is a bit complex but follows a logical sequence. It uses a mixture of Python features: mapping, filtering, and summing. Here's what it does step by step:
     - `map(str, arr)`: This converts each element in the input array arr to a string.
     - `b != '-'`: This line filters out elements where the first character (b) is a hyphen '-', avoiding negative numbers.
     - `sum(int(d) for d in str(b))`: This calculates the sum of the digits of each element b after it has been converted to a string. It uses a generator expression to iterate through each character in the string representation of b and converts it to an integer.
     - `> 0`: This condition checks if the sum of the digits is greater than 0.
    - `sum(...)`: Finally, this line counts the elements that satisfy the condition and returns their count.
3. `return output`: This line returns the result of the counting process, which is the number of elements in the input array with a positive digit sum.

Overall, the function is designed to efficiently determine the count of elements in the array that have a positive digit sum, as described in the test cases provided.