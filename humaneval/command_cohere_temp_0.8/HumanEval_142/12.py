```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```
This function takes as input a list of integers and squares every integer in the list if its index is a multiple of 3. It cubes every 
integer in the list if its index is a multiple of 4 but not a multiple of 3. The function does not alter the list's elements 
if their indexes are not a multiple of 3 or 4. Finally, it returns the sum of all list elements. 

Here's an example of function usage:
```python
my_list = [1, 2, 3]
print(f'The sum of squared integers is {sum_squares(my_list)}')
```
This would output "The sum of squared integers is 6" 

And here is the expected outcome for the provided test cases:
For lst = [1,2,3] the output should be 6
Sum is calculated as follows: 1**2 + 2**2 + 3**2 = 1 + 4 + 9 = 6

For lst = []  the output should be 0
Sum is calculated as follows: 0**2 + 0**2 + 0**2 = 0 + 0 + 0 = 0

For lst = [-1,-5,2,-1,-5]  the output should be -126
Sum is calculated as follows: -1**2 + -5**2 + 2**2 + -1**2 + -5**2 = 1 + 25 + 4 + 1 + 25 = 126
```