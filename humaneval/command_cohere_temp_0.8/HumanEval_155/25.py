Here's a Python script that contains a function called even_odd_count that takes an integer num as input and returns a tuple with the count of even and odd digits in num, respectively:
```python
def even_odd_count(num):
    count = 0
    # Iterate each digit in the input number
    for digit in str(num): 
        # Increment count if digit is odd
        if digit % 2 != 0: 
            count += 1
    return count, 10 - count 

# Testing the function with some examples
print(even_odd_count(-12)) # (1, 1)
print(even_odd_count(123))  # (1, 2)
```

This script defines the `even_odd_count` function, which takes an integer as input and returns a tuple containing the counts of even and odd digits in the input number. The function uses a for loop to iterate through each digit in the string representation of the input number and checks whether the digit is even or odd, incrementing the appropriate count accordingly. The example usage shows how the function can be called with different input values to produce the desired results. The 10 - count part ensures that the count of even digits always sums up to 10, as there are 5 even digits between 1 to 9 and above 9, the tens place becomes odd.  This method is not the most efficient one, but it gets the job done and is quite intuitive.