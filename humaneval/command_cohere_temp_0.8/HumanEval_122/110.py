Here's a Python script that contains a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            sum_two_digits += arr[i]
    return sum_two_digits
```
This script defines a function called `add_elements` that takes in two arguments, an array `arr` and an integer `k`. The function sums up any element from the first `k` elements of `arr` that has at most 2 digits in its decimal representation. It does so by iterating through the first `k` elements of the array using a for loop. It then checks if the length of the string representation of that element is less than or equal to 2. If so, it adds the value of that element to the running sum `sum_two_digits`. Finally, the function returns the value of `sum_two_digits`.