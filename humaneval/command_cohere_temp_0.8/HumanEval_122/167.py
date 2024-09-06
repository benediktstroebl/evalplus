Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k): 
        num = arr[i]
        if len(str(num))<=2:
            sum_two_digits += num  
    return sum_two_digits

# Example usage
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
result = add_elements(arr, k)
print(f'Example output: {result}')

```
This script defines a function called `add_elements` that takes in an array `arr` and an integer `k`. The function sums the elements in `arr` that have at most two digits from the first `k` elements of `arr`. The script also includes an example usage of this function with a specific input and prints the resulting output. 

Let's examine the code for a deeper understanding. The inner loop on the array iterates through the first `k` elements, and the condition `len(str(num))<=2` checks if the length of the string representation of the integer `num` is less than or equal to 2. If the condition is true, the integer is added to the `sum_two_digits` variable. Finally, the function returns the total sum of the integers that meet the condition. 

The example usage included demonstrates the function on a specific input and prints the output. Overall, the script solves the problem as stated and provides an insightful example for understanding.