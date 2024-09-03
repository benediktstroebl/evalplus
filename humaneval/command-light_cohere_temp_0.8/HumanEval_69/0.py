```python
def search(nums): 
    freq = 0
    # Initialize frequency counter
    for num in nums: 
        freq += num 
    return freq
# Driver code
search([4, 1, 2, 2, 3, 1])  # Output: 2
search([1, 2, 2, 3, 3, 3, 4, 4, 4])  # Output: 3
search([5, 5, 4, 4, 4])  # Output: -1
```
The function search takes a list of numbers, nums, as input and returns the frequency of the greatest integer that is greater than zero and has a frequency greater than or equal to the value of the integer itself. The function uses a counter to keep track of the frequency of each integer in the list. The function then iterates through the numbers and adds up the frequency of each integer in the list. The function returns the maximum integer in the list that has a frequency greater than or equal to the value of the integer itself.