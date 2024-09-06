```python
def count_nums(arr):
    nums = [int(i) for i in arr]
    count = 0
    for n in nums:
        if sum(int(d) for d in str(n)) > 0:
            count += 1
    return count
```

This function takes an array of integers `arr` as input and returns the number of elements in the array that have a sum of their digits greater than 0. The function achieves this by first converting each element in the array to an integer using a list comprehension. It then iterates through each integer in the list and checks if the sum of the digits of each integer is greater than 0, using a generator expression within the sum function to extract the individual digits of the integer represented as a string. Finally, it returns the count of elements with the described property. 

This solution is encapsulated in a standalone function that can be imported and executed independently, as evidenced by the provided tests in the original problem statement. Thus, this function is both standalone and reusable for solving this specific problem.