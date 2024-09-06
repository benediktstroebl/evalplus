```python
def odd_count(lst):
    r = []
    for digits in lst:
        count = 0
        for i in range(len(digits)):
            if int(digits[i]) % 2:
                count += 1
        r.append(f"the number of odd elements in the string {count} of the input")
    return r
```

This code solves the problem by doing the following:
- The code defines a function `odd_count` that takes in a list of lists, where each inner list represents a string of digits.
- It initializes an empty list called `r` to store the results.
- The function then iterates through each inner list (string) of the input list.
- For each character in the string, it checks if the digit is odd or even using the modulo operator (`int(digits[i]) % 2`) and increments a count if it is odd.
- Finally, it appends to the `r` list a formatted string indicating the count of odd digits in the string with the specified number, and returns the `r` list containing the results. 

The expected output for the provided test cases is:
```
['the number of odd elements in the string 4 of the input']
['the number of odd elements in the string 1 of the input', 'the number of odd elements in the string 8 of the input']
``` 

This solution is efficient and straightforward, using a single loop to iterate through the input lists and correctly counts odd digits.